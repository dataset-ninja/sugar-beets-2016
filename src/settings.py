from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Sugar Beets 2016"
PROJECT_NAME_FULL: str = "Sugar Beets 2016: Agricultural Robot Dataset for Plant Classification, Localization and Mapping on Sugar Beet Fields"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Agricultural(), Industry.Robotics()]
CATEGORY: Category = Category.Agriculture(extra=Category.Robotics())

CV_TASKS: List[CVTask] = [CVTask.InstanceSegmentation(), CVTask.SemanticSegmentation(), CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2016

HOMEPAGE_URL: str = "https://www.ipb.uni-bonn.de/data/sugarbeets2016/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 4690401
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/sugar-beets-2016"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = "https://www.ipb.uni-bonn.de/datasets_IJRR2017"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {"sugar beet": [255, 0, 255], "weed": [255, 0, 0]}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
PAPER: Optional[
    Union[str, List[str]]
] = "https://journals.sagepub.com/doi/full/10.1177/0278364917720510"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    'Software Tools': "https://github.com/PRBonn/pybonirob",
    "Repository": "https://www.ipb.uni-bonn.de/datasets_IJRR2017/"
}

CITATION_URL: Optional[str] = "https://www.ipb.uni-bonn.de/data/sugarbeets2016/"
AUTHORS: Optional[List[str]] = [
    "Nived Chebrolu",
    "Philipp Lottes",
    "Alexander Schaefer",
    "Wera Winterhalter",
    "Wolfram Burgard",
    "Cyrill Stachniss",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["photogrammetry@uni-bonn.de"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "University of Bonn, Germany",
    "University of Freiburg, Germany",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.uni-bonn.de/en/university/university",
    "https://uni-freiburg.de/en/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "__PRETEXT__": "Additionally, every image contains information about ***im_id***, ***location*** and ***date***"
}
TAGS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
