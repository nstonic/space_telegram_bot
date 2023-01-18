import argparse
import os
import random
import time
from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_images
import telegram
from dotenv import load_dotenv
from files_and_dirs import resize_image


def publish_photo(image_file_path: str):
    load_dotenv()
    resize_image(image_file_path)
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_API'])
    bot.send_photo(chat_id="@nstonic_SpacePhotos", photo=open(image_file_path, "rb"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image",
                        help="Путь к файлу с фотографией")
    args = parser.parse_args()

    if image_file_path := args.image:
        publish_photo(image_file_path)
    else:
        while True:
            fetch_spacex_images()
            fetch_nasa_apod(10)
            fetch_nasa_epic(10)
            images = os.listdir("images")
            publish_photo(f"images/{random.choice(images)}")

            if os.getenv('DELAY_SECONDS'):
                delay = int(os.getenv('DELAY_SECONDS'))
            else:
                delay = 14400

            time.sleep(delay)


if __name__ == '__main__':
    main()
