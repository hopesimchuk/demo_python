"""
Импортируем методы и функции
"""
from requests import get
from random import choice
import classes

"""
Добавляем сссылку на файл со словами для игры
"""
URL_DB = r"https://jsonkeeper.com/b/JTQY"

"""
Функция для загрузки словаря из json файла, удаление дублей и и рандомный выбор слова для игры
"""


def load_random_word(url: str = URL_DB):
    user_db = get(url).json()

    for item in user_db:
        item["subwords"] = list(set(item["subwords"]))

    user_db_item = choice(user_db)
    word_game = classes.BasicWord(
        raw_word=user_db_item["word"],
        lst_word=user_db_item["subwords"]
    )
    return word_game
