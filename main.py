from dotenv import load_dotenv
from api import *
from files_and_dirs import *


def fetch_spacex_last_launch():
    try:
        latest_launch_links = get_links_from_spacex()
    except:
        return

    for index, link in enumerate(latest_launch_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/spacex-{index:0>4d}{ext}")
        except:
            continue


def fetch_nasa_apod():
    """
        APOD is the Astronomy Picture of the Day
    """
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    try:
        nasa_apod_links = get_nasa_apod_links(nasa_api_key)
    except:
        return

    for index, link in enumerate(nasa_apod_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/nasa-apod-{index:0>4d}{ext}")
        except:
            continue


def fetch_nasa_epic():
    """
        EPIC is the Earth Polychromatic Imaging Camera
    """
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    try:
        nasa_epic_links = get_nasa_epic_links(nasa_api_key)
    except:
        return

    for index, link in enumerate(nasa_epic_links):
        try:
            ext = get_file_ext(link)
            download_image(url=link,
                           target_path=f"images/nasa-epic-{index:0>4d}{ext}")
        except:
            continue


def main():
    fetch_nasa_apod()
    fetch_spacex_last_launch()
    fetch_nasa_epic()


if __name__ == '__main__':
    main()
