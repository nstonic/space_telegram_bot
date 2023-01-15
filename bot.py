import os
import random
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    images = os.listdir("images")
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_API'))
    bot.send_photo(chat_id="@nstonic_SpacePhotos", photo=open(f"images/{random.choice(images)}", "rb"))


if __name__ == '__main__':
    main()
