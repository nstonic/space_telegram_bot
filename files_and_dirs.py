import os

import requests
from urllib.parse import urlparse, unquote
from PIL import Image


def get_file_ext(url: str) -> str:
    parsed_link = urlparse(url)
    unquoted_path = unquote(parsed_link.path)
    return os.path.splitext(unquoted_path)[1]


def download_image(url: str, target_path: str):
    os.makedirs("images", exist_ok=True)
    image_response = requests.get(url)
    image_response.raise_for_status()
    with open(target_path, "wb") as file:
        file.write(image_response.content)
    print("Image downloaded:", url)


def resize_image(image_file: str, long_side: int = 2048):
    with Image.open(image_file) as image:
        image.thumbnail((long_side, long_side))
        image.save(image_file)
