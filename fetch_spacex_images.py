import os

import requests
import argparse

from files_and_dirs import get_file_ext, download_image


def get_links_from_spacex(launch_id: str) -> list[str]:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_images(launch_id: str):
    try:
        launch_links = get_links_from_spacex(launch_id)
    except requests.exceptions.HTTPError as ex:
        print(ex)
        return

    if not len(launch_links):
        print("К этому запуску нет фотографий.")
        return

    for index, link in enumerate(launch_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=os.path.join("images", f"spacex-{index:0>4d}{ext}"))
        except requests.exceptions.HTTPError as ex:
            print(ex)
            continue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id",
                        dest="launch_id",
                        default="latest",
                        help="ID запуска. Если не указан, то загружается последний запуск")
    args = parser.parse_args()
    fetch_spacex_images(args.launch_id)


if __name__ == '__main__':
    main()
