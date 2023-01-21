import os
import random
import time

import argparse
import telegram
from dotenv import load_dotenv

from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_images
from files_and_dirs import resize_image


def publish_photo(image_file_path: str, telegram_bot_token: str, chat_id: str):
    resize_image(image_file_path)
    bot = telegram.Bot(token=telegram_bot_token)
    with open(image_file_path, "rb") as image_file:
        bot.send_photo(chat_id=chat_id, photo=image_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image",
                        help="Путь к файлу с фотографией")
    args = parser.parse_args()
    load_dotenv()
    chat_id = os.environ["TG_CHAT_ID"]
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]

    if image_file_path := args.image:
        publish_photo(image_file_path, telegram_bot_token, chat_id)
    else:
        while True:
            images = os.listdir("images")
            publish_photo(os.path.join("images", f"{random.choice(images)}"), telegram_bot_token, chat_id)
            delay = int(os.getenv('DELAY_SECONDS', default=14400))
            time.sleep(delay)


if __name__ == '__main__':
    main()
