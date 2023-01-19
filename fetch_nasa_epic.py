import argparse
from datetime import datetime
import os
import requests
from dotenv import load_dotenv
from files_and_dirs import get_file_ext, download_image


def get_nasa_epic_links(image_count: int, api_key: str) -> list[str]:
    params = {
        "api_key": api_key,
        "count": image_count
    }

    nasa_epic_response = requests.get("https://api.nasa.gov/EPIC/api/natural/images",
                                      params=params)
    nasa_epic_response.raise_for_status()
    links = []
    for image in nasa_epic_response.json():
        image_date = datetime.fromisoformat(image["date"])
        image_name = image["image"]
        links.append(f"https://epic.gsfc.nasa.gov/archive/natural/{image_date.strftime('%Y/%m/%d')}/jpg/{image_name}.jpg")
    return links


def fetch_nasa_epic(image_count: int, api_key: str):
    """
        EPIC is the Earth Polychromatic Imaging Camera
    """

    try:
        nasa_epic_links = get_nasa_epic_links(image_count, api_key)
    except requests.exceptions.HTTPError as ex:
        print(ex)
        return

    for index, link in enumerate(nasa_epic_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=os.path.join("images", f"nasa-epic-{index:0>4d}{ext}"))
        except requests.exceptions.HTTPError as ex:
            print(ex)
            continue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count",
                        type=int,
                        help="Количество загружаемых фотографий. По умолчанию 1")
    args = parser.parse_args()
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    fetch_nasa_epic(image_count=args.count or 1, api_key=nasa_api_key)


if __name__ == '__main__':
    main()
