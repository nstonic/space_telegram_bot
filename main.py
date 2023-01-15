import os
import random
import time
from PIL import Image
from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_images
import telegram
from dotenv import load_dotenv
from files_and_dirs import resize_image


def main():
    while True:
        fetch_spacex_images()
        fetch_nasa_apod(10)
        fetch_nasa_epic(10)

        load_dotenv()
        images = os.listdir("images")
        image_file = f"images/{random.choice(images)}"
        resize_image(image_file)

        bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_API'))
        bot.send_photo(chat_id="@nstonic_SpacePhotos", photo=open(image_file, "rb"))

        if os.getenv('DELAY_SECONDS'):
            delay = int(os.getenv('DELAY_SECONDS'))
        else:
            delay = 14400

        time.sleep(delay)


if __name__ == '__main__':
    main()
