# Google Images Download using Selenium

> 본 파이썬 모듈은 https://pypi.org/project/google_images_download/ 위 모듈이 구글 크롬의 업데이트로 사용 불가능해진 것에 대한 대안으로 Selenium을 이용한 크롤링 과정을 간편화한 모듈입니다.  

## Install

```bash
pip install gids
```

## Usage

```python
from gids import builder

config = {
    'driver_path': './chromedriver',
    'headless': True,
    'window-size': '720x480',
    'disable_gpu': False
}

first_item = {
    'keyword': 'Lion',
    'limit': 10, # The number of images
    'download_context': './data',
    'path': 'animal' # save in ./data/animal/img_01...10
}

second_item = {
    'keyword': 'Bamboo',
    'limit': 10, # The number of images
    'download_context': './data',
    'path': 'plant' # save in ./data/plant/img_01...10
}

items = [first_item, second_item]

downloader = builder.build(config)

downloader.download(items)
```
