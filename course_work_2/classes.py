class BasicWord():
    """
    Создаем метод:
    который проверяет введенное слово в списке допустимых подслов,
    который ведет подчсет количества слов
    """
    def __init__(self, word_original: str, word_list: list) -> None:
        self.word_original = word_original
        self.word_list = word_list

    def check_user_input(self, usr_word: str) -> bool:
        return usr_word in self.word_list

    def word_count(self) -> int:
        return len(self.word_list)


class Player():
    """
    Создаем метод:
    который ведет подчсет количества слов,
    который добавляет слово в использованные слова,
    который проверяет слова на уникальнось
    """

    def __init__(self, user_name: str) -> None:
        self.user_name = user_name

    def word_count(self) -> int:
        return len(self.word_list)

    def list_append(self, word_append: str) -> bool:
        self.word_append = word_append

        if not self.word_unique(word_append):
            self.word_list.append(word_append)

    def word_unique(self, word_append: str) -> int:
        return word_unique in self.word_list
