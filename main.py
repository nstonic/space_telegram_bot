from dotenv import load_dotenv
from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_images


def main():
    fetch_nasa_apod()
    fetch_spacex_images()
    fetch_nasa_epic()


if __name__ == '__main__':
    main()
