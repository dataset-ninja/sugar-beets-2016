Dataset **Sugar Beets 2016** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/m/A/de/UbsRTdrNff2YVueoC4x0TcD8xiQUL87RDahC1TvprTMSCZgYppWgOuUJKqrhpzTO0s06eMYM7EQpfOtQ7weMJjITy8G6iZFraPEGFPRDBH8PXOB9svvbLWzm8rzB.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Sugar Beets 2016', dst_path='~/dtools/datasets/Sugar Beets 2016.tar')
```
The data in original format can be 🔗[downloaded here](https://www.ipb.uni-bonn.de/datasets_IJRR2017)