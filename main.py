from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_images


def main():
    fetch_spacex_images()
    fetch_nasa_apod(50)
    fetch_nasa_epic(50)


if __name__ == '__main__':
    main()
