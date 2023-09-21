# https://www.ipb.uni-bonn.de/data/sugarbeets2016/

import os
import shutil
from urllib.parse import unquote, urlparse

import cv2
import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_name,
    get_file_name_with_ext,
)
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer...", total=fsize) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Sugar Beets 2016"
    dataset_path = "/home/grokhi/rawdata/sugar-beets-2016/ijrr_sugarbeets_2016_annotations" 

    images_subpath = "images/rgb"
    nir_subpath = "images/nir"
    masks_subpath = "annotations/dlp/colorCleaned"
    images_shape = (1296, 966)
    batch_size = 100
    ds_name = "ds"
    group_tag_name = "im_id"

    colors = []

    def get_unique_colors(img):
        unique_colors = []
        img = img.astype(np.int32)
        h, w = img.shape[:2]
        colhash = img[:, :, 0] * 256 * 256 + img[:, :, 1] * 256 + img[:, :, 2]
        unq, unq_inv, unq_cnt = np.unique(colhash, return_inverse=True, return_counts=True)
        indxs = np.split(np.argsort(unq_inv), np.cumsum(unq_cnt[:-1]))
        col2indx = {unq[i]: indxs[i][0] for i in range(len(unq))}
        for col, indx in col2indx.items():
            if col != 0:
                unique_colors.append((col // (256**2), (col // 256) % 256, col % 256))

        return unique_colors

    def create_ann(image_path):
        labels = []
        tags = []

        id_data = get_file_name(image_path)
        group_id = sly.Tag(tag_id, value=id_data)
        tags.append(group_id)

        tag_location = sly.Tag(location, value="Campus Klein Altendorf")
        tags.append(tag_location)

        date_value = subfolder.split("_")[1]
        if date_value != "weed":
            tag_date = sly.Tag(date, value=date_value)
            tags.append(tag_date)

        mask_path = os.path.join(masks_path, get_file_name_with_ext(image_path))
        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)
            unique_colors = get_unique_colors(mask_np)
            for curr_color in unique_colors:
                if curr_color not in colors:
                    colors.append(curr_color)
            for color in unique_colors:
                mask = np.all(mask_np == color, axis=2)
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    bitmap = sly.Bitmap(data=obj_mask)
                    if bitmap.area > 150:
                        obj_class = color_to_obj_class[color]
                        label = sly.Label(bitmap, obj_class)
                        labels.append(label)

        return sly.Annotation(
            img_size=(images_shape[1], images_shape[0]), labels=labels, img_tags=tags
        )

    color_to_obj_class = {
        (0, 255, 0): sly.ObjClass("sugar beet", sly.Bitmap, color=(0, 255, 0)),
        (255, 0, 0): sly.ObjClass("weed", sly.Bitmap, color=(255, 0, 0)),
    }

    location = sly.TagMeta("location", sly.TagValueType.ANY_STRING)
    date = sly.TagMeta("date", sly.TagValueType.ANY_STRING)
    tag_id = sly.TagMeta("im_id", sly.TagValueType.ANY_STRING)

    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    meta = sly.ProjectMeta(
        obj_classes=list(color_to_obj_class.values()), tag_metas=[location, date]
    )
    meta = meta.add_tag_meta(group_tag_meta)
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    for subfolder in os.listdir(dataset_path):
        curr_folder_path = os.path.join(dataset_path, subfolder)
        if dir_exists(curr_folder_path):
            images_path = os.path.join(curr_folder_path, images_subpath)
            nir_path = os.path.join(curr_folder_path, nir_subpath)
            masks_path = os.path.join(curr_folder_path, masks_subpath)
            for curr_images_path in [images_path, nir_path]:
                images_names = os.listdir(curr_images_path)

                progress = sly.Progress(
                    "Create dataset {}, add {} data".format(ds_name, subfolder), len(images_names)
                )

                for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                    images_path_batch = [
                        os.path.join(curr_images_path, image_name)
                        for image_name in images_names_batch
                    ]

                    images_names_batch = [
                        im_path.split("/")[-2] + "_" + get_file_name_with_ext(im_path)
                        for im_path in images_path_batch
                    ]

                    img_infos = api.image.upload_paths(
                        dataset.id, images_names_batch, images_path_batch
                    )
                    img_ids = [im_info.id for im_info in img_infos]

                    anns_batch = [create_ann(image_path) for image_path in images_path_batch]
                    api.annotation.upload_anns(img_ids, anns_batch)

                    progress.iters_done_report(len(images_path_batch))
    return project
