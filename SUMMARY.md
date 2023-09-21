**Sugar Beets 2016: Agricultural Robot Dataset for Plant Classification, Localization and Mapping on Sugar Beet Fields** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the agricultural and robotics industries. 

The dataset consists of 25429 images with 110084 labeled objects belonging to 2 different classes including *sugar beet* and *weed*.

Images in the Sugar Beets 2016 dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 3209 (13% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Additionally, every image contains information about ***im_id***, ***location*** and ***date***. The dataset was released in 2016 by the University of Bonn, Germany and University of Freiburg, Germany.

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/sugar-beets-2016/raw/main/visualizations/horizontal_grid.png">
