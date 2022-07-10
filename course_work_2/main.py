import classes
import utils
from random import choice

"""
Функция для приветствия
"""


def start(player, word_append) -> None:
    print(
        f"Привет, {player.user_name}\n"
        f"Составь {word_append.word_count()} слов  из слова {word_append.word_original}\n"
        f"Слова не должны быть короче 3 букв\n"
        f"Чтобы закончить игру, угадайте все слова или напишите stop\n"
        f"Поехали, ваше первое слово?\n"
    )


"""
Функция для показа статистики
"""


def statistic(player) -> None:
    print(
        f"Игра завершена, вы угадали {player.word_count} слов!"
    )


def main():
    """
    Создаем экземпляр класса Player
    """
    player = classes.Player(input("Введите ваше имя: \t"))

    """
    Создаем экземпляр класса BasicWord
    """
    word_append = utils.load_random_word()
    start(player, word_append)

    i = 0
    while i != word_append.word_count():
        user_input = str(input(">>>")).lower()
        if user_input in ("stop", "стоп"):
            print("Игра закончена")
            quit()
        elif player.word_unique(user_input):
            print("Вы уже так отвечали, введите другой ответ")
        elif word_append.check_user_input(user_input):
            print("Молодец, такое слово есть!")
        else:
            print("Такого слова нет, введите другой ответ")
        i += 1

        statistic(player)




