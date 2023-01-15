import os

from fetch_nasa_apod import fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from fetch_spacex_images import fetch_spacex_images
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_API'))
    bot.send_message(chat_id="@nstonic_SpacePhotos", text="Всем привет!")

    # fetch_spacex_images()
    # fetch_nasa_apod(50)
    # fetch_nasa_epic(50)


if __name__ == '__main__':
    main()
