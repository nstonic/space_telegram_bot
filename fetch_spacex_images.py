import requests
from files_and_dirs import get_file_ext, download_image
import argparse


def get_links_from_spacex(launch_id) -> list[str]:
    params = {}
    latest = "latest"
    if launch_id:
        params = {"id": launch_id}
        latest = ""
    spacex_launch_responce = requests.get(f"https://api.spacexdata.com/v5/launches/{latest}", params=params)
    spacex_launch_responce.raise_for_status()
    if launch_id:
        for launch in spacex_launch_responce.json():
            if launch["id"] == launch_id:
                return launch["links"]["flickr"]["original"]
    return spacex_launch_responce.json()["links"]["flickr"]["original"]


def fetch_spacex_images(launch_id: str = None):
    try:
        launch_links = get_links_from_spacex(launch_id)
    except Exception as ex:
        print(ex)
        return

    if not len(launch_links):
        print("К этому запуску нет фотографий.")
        return

    for index, link in enumerate(launch_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/spacex-{index:0>4d}{ext}")
        except:
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--id",
                        help="id запуска. Если не указан, то загружается последний запуск")
    args = parser.parse_args()
    launch_id = args.id
    fetch_spacex_images(launch_id)
