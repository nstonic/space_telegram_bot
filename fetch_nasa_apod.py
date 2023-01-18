import argparse
import os
import requests
from dotenv import load_dotenv
from files_and_dirs import get_file_ext, download_image


def get_nasa_apod_links(image_count) -> list[str]:
    load_dotenv()
    params = {
        "api_key": os.environ["NASA_API_KEY"],
        "count": image_count
    }

    nasa_apod_response = requests.get("https://api.nasa.gov/planetary/apod",
                                      params=params)
    nasa_apod_response.raise_for_status()
    links = []
    for apod in nasa_apod_response.json():
        if link := apod.get("hdurl"):
            links.append(link)
    return links


def fetch_nasa_apod(image_count: int = 1):
    """
        APOD is the Astronomy Picture of the Day
    """

    try:
        nasa_apod_links = get_nasa_apod_links(image_count)
    except requests.exceptions.HTTPError as ex:
        print(ex)
        return

    for index, link in enumerate(nasa_apod_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/nasa-apod-{index:0>4d}{ext}")
        except requests.exceptions.HTTPError as ex:
            print(ex)
            continue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count",
                        type=int,
                        help="Количество загружаемых фотографий. По умолчанию 1")
    args = parser.parse_args()
    if image_count := args.count:
        fetch_nasa_apod(image_count)
    else:
        fetch_nasa_apod()


if __name__ == '__main__':
    main()
