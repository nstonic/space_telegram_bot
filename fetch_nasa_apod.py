import argparse
import os
import requests
from dotenv import load_dotenv
from files_and_dirs import get_file_ext, download_image


def get_nasa_apod_links(image_count) -> list[str]:
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    params = {
        "api_key": nasa_api_key,
        "count": image_count
    }

    nasa_apod_responce = requests.get("https://api.nasa.gov/planetary/apod",
                                      params=params)
    nasa_apod_responce.raise_for_status()
    links = []
    for apod in nasa_apod_responce.json():
        if link := apod.get("hdurl"):
            links.append(link)
    return links


def fetch_nasa_apod(image_count: int = 50):
    """
        APOD is the Astronomy Picture of the Day
    """
    try:
        nasa_apod_links = get_nasa_apod_links(image_count)
    except Exception as ex:
        print(ex)
        return

    for index, link in enumerate(nasa_apod_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/nasa-apod-{index:0>4d}{ext}")
        except:
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--count",
                        type=int,
                        help="Количество загружаемых фотографий. По умолчанию 50")
    args = parser.parse_args()
    image_count = args.count
    fetch_nasa_apod(image_count)
