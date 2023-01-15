import argparse
import os
import requests
from dotenv import load_dotenv
from files_and_dirs import get_file_ext, download_image


def get_nasa_epic_links(image_count: int) -> list[str]:
    load_dotenv()
    params = {
        "api_key": os.getenv("NASA_API_KEY"),
        "count": image_count
    }

    nasa_epic_responce = requests.get("https://api.nasa.gov/EPIC/api/natural/images",
                                      params=params)
    links = []
    for image in nasa_epic_responce.json():
        image_date = image["date"].split()[0].replace("-", "/")
        image_name = image["image"]
        links.append(f"https://epic.gsfc.nasa.gov/archive/natural/{image_date}/jpg/{image_name}.jpg")
    return links


def fetch_nasa_epic(image_count: int = 1):
    """
        EPIC is the Earth Polychromatic Imaging Camera
    """

    try:
        nasa_epic_links = get_nasa_epic_links(image_count)
    except Exception as ex:
        print(ex)
        return

    for index, link in enumerate(nasa_epic_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/nasa-epic-{index:0>4d}{ext}")
        except:
            continue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count",
                        type=int,
                        help="Количество загружаемых фотографий. По умолчанию 1")
    args = parser.parse_args()
    if image_count := args.count:
        fetch_nasa_epic(image_count)
    else:
        fetch_nasa_epic()


if __name__ == '__main__':
    main()
