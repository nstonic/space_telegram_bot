from dotenv import load_dotenv
from api import *
from files_and_dirs import *
from fetch_spacex_images import fetch_spacex_images


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
    fetch_spacex_images()
    fetch_nasa_epic()


if __name__ == '__main__':
    main()
