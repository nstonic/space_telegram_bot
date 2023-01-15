import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote


def get_file_extension(url: str) -> str:
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


def get_links_from_spacex() -> list:
    spacex_launch_responce = requests.get("https://api.spacexdata.com/v5/launches/latest")
    spacex_launch_responce.raise_for_status()
    return spacex_launch_responce["links"]["flickr"]["original"]


def get_nasa_apod_links() -> list:
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    params = {
        "api_key": nasa_api_key,
        "count": 30
    }

    nasa_apod_responce = requests.get("https://api.nasa.gov/planetary/apod",
                                      params=params)
    nasa_apod_responce.raise_for_status()
    links = []
    for apod in nasa_apod_responce.json():
        if link := apod.get("hdurl"):
            links.append(link)
    return links


def fetch_spacex_last_launch():
    try:
        latest_launch_links = get_links_from_spacex()
    except:
        return

    for index, link in enumerate(latest_launch_links):
        print(link)
        ext = get_file_extension(link)
        download_image(url=link,
                       target_path=f"images/spacex-{index}.{ext}")


def fetch_nasa_apod():
    """
        APOD is the Astronomy Picture of the Day
    """
    try:
        nasa_apod_links = get_nasa_apod_links()
    except:
        return

    for index, link in enumerate(nasa_apod_links):
        print(link)
        ext = get_file_extension(link)
        download_image(url=link,
                       target_path=f"images/nasa-{index}.{ext}")


if __name__ == '__main__':
    fetch_nasa_apod()
    fetch_spacex_last_launch()
