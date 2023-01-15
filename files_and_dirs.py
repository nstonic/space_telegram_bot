import os
from urllib.parse import urlparse, unquote

import requests


def get_file_ext(url: str) -> str:
    parsed_link = urlparse(url)
    unquoted_path = unquote(parsed_link.path)
    return os.path.splitext(unquoted_path)[1]


def download_image(url: str, target_path: str):
    if not os.path.isdir("images"):
        os.mkdir("images")
    jpeg_responce = requests.get(url)
    jpeg_responce.raise_for_status()
    with open(target_path, "wb") as file:
        file.write(jpeg_responce.content)
