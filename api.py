import requests


def get_links_from_spacex() -> list[str]:
    spacex_launch_responce = requests.get("https://api.spacexdata.com/v5/launches/latest")
    spacex_launch_responce.raise_for_status()
    return spacex_launch_responce["links"]["flickr"]["original"]


def get_nasa_apod_links(nasa_api_key: str) -> list[str]:
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


def get_nasa_epic_links(nasa_api_key: str) -> list[str]:
    params = {
        "api_key": nasa_api_key,
        "count": 30
    }

    nasa_epic_responce = requests.get("https://api.nasa.gov/EPIC/api/natural/images",
                                      params=params)
    links = []
    for image in nasa_epic_responce.json():
        image_date = image["date"].split()[0].replace("-", "/")
        image_name = image["image"]
        links.append(f"https://epic.gsfc.nasa.gov/archive/natural/{image_date}/jpg/{image_name}.jpg")
    return links
