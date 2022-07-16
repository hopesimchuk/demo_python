import classes
import utils

"""
Функция для приветствия
"""


def start(player, word) -> None:
    print(
        f"Привет, {player.name}\n"
        f"Составь {word.lst_word_cnt()} слов  из слова {word.raw_word}\n"
        f"Слова не должны быть короче 3 букв\n"
        f"Чтобы закончить игру, угадайте все слова или напишите stop\n"
        f"Поехали, ваше первое слово?\n"
    )


"""
Функция для показа статистики
"""


def statistic(player) -> None:
    print(
        f"Игра завершена, вы угадали {player.lst_word_cnt()} слов!"
    )


def main():
    """
    Создаем экземпляр класса Player
    """
    player = classes.Player(input("Введите ваше имя: \t"))

    """
    Создаем экземпляр класса BasicWord
    """
    word = utils.load_random_word()
    start(player, word)

    i = 0
    while i != word.lst_word_cnt():
        user_input = str(input(">>>")).lower()
        if user_input in ("stop", "стоп"):
            print("Игра закончена")
            quit()
        elif player.word_already_used(user_input):
            print("Вы уже так отвечали, введите другой ответ")
        elif word.check_usr_input(user_input):
            print("Молодец, такое слово есть!")
        else:
            print("Такого слова нет, введите другой ответ")
        i += 1
    statistic(player)


main()
