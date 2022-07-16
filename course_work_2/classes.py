class BasicWord():
    """
    Создаем метод:
    который проверяет введенное слово в списке допустимых подслов,
    который ведет подчсет количества слов
    """

    def __init__(self, raw_word: str, lst_word: list) -> None:
        self.raw_word = raw_word
        self.lst_word = lst_word

    def check_usr_input(self, usr_word: str) -> bool:
        return usr_word in self.lst_word

    def lst_word_cnt(self) -> int:
        return len(self.lst_word)


class Player():
    """
    Создаем метод:
    который ведет подчсет количества слов,
    который добавляет слово в использованные слова,
    который проверяет слова на уникальнось
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.lst_word = []

    def lst_word_cnt(self) -> int:
        return len(self.lst_word)

    def list_append(self, word: str) -> None:
        if not self.word_already_used(word):
            self.lst_word.append(word)

    def word_already_used(self, word: str) -> bool:
        return word in self.lst_word
