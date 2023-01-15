# Телеграм-бот с космическими фотографиями

Космическое агнтство НАСА и компания SpaceX предоставляют открыт доступ к своей базе фотографий.
Данный скрипт запускает телеграм-бота, который с заданной периодичностью публикует актуальные фотографии из этих баз.

### Как установить

- Python3 должен быть уже установлен.
- Затем используйте `pip` для установки необходимых компонентов:

```
pip install -r requirements.txt
```

- Затем необходимо создать бота с помощью [@BotFather](https://t.me/BotFather). Как им пользоваться, можно
  почитать [здесь](https://chatlabs.ru/botfather-instrukcziya-komandy-nastrojki/). Полученный от него токен необходимо
  поместить в переменную **TELEGRAM_BOT_API** в файле .env
- Вам также понадобится получить токен на сайте НАСА. Сделать это проще простого по ссылке https://api.nasa.gov/. Этот
  токен необходимо поместить в переменную **NASA_API_KEY** в файле .env
- Кроме того, в файле .env можно создать переменную **DELAY_SECONDS**. Данная переменная определяет период в секундах,
  через который бот будет загружать и постить новые фото. Если данная переменная не задана, то это будет происходить каждые
  4 часа

### Как пользоваться

- Для запуска бота в командной строке перейдите в папку в которой лежит файл main.py. Затем запустит скрипт следующей
  командой

```
python main.py
```

- Так же можно вручную запустить сбор фотографий. Сделать это можно с помощью файлов:
    - fetch_spacex_images.py
    - fetch_nasa_apod.py
    - fetch_nasa_epic.py

- Файл fetch_spacex_images.py собирает фотографии запусков SpaceX. Используйте следующую команду:

  ```
  python fetch_spacex_images.py --id=some_id
  ``` 

    - параметр id - это id конкретного запуска. Если не указан, то загружается последний запуск


- Файл fetch_nasa_apod.py собирает фотографии с сервиса Astronomy Picture of the Day (Астрономическое фото дня).
  Используйте следующую команду:
  ```
  python fetch_nasa_apod.py --count=50
  ```
    - параметр count - это количество загружаемых фото. Если н указано, то загружается одна.

- Файл fetch_nasa_epic.py собирает фотографии с сервиса Earth Polychromatic Imaging Camera (Камера полихроматического
  изображения Земли).
  Используйте следующую команду:
  ```
  python fetch_nasa_epic.py --count=50
  ```
    - параметр count - это количество загружаемых фото. Если н указано, то загружается одна.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).