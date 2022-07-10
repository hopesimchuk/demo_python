"""
Импортируем методы и функции
"""
from requests import get
from random import choice
import classes

"""
Добавляем сссылку на файл со словами для игры
"""
URL_DN = r"https://jsonkeeper.com/b/GUIW"

"""
Функция для загрузки словаря из json файла, удаление дублей и и рандомный выбор слова для игры
"""
def load_random_word(json_file):
    user_word = get(json_file).json()

    for item in user_word:
        item["words"] = list(set(item["words"]))

    user_word_item = choice(user_word)
    word_game = classes.BasicWord(
        word_original = user_word_item["word"],
        word_list = user_word_item["words"]
    )
    return word_game
