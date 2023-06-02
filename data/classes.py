# Класс для работы с полученным словом и его списком подслов.
class BasicWord:
    def __init__(self, default_word, sub_words):
        self.default_word = default_word
        self.sub_words = sub_words

    def __repr__(self):
        return f'Экземпляр класса "BasicWord", который содержит в себе "{self.default_word}" и {self.sub_words}'

    def check_word(self, word):
        """Проверка введенного слова в списке допустимых подслов."""
        if word in self.sub_words:
            return True

    def len_sub_words(self):
        """Подсчет количества подслов."""
        return int(len(self.sub_words))


# Класс для учёта действий игрока.
class Player:
    def __init__(self, user_name, used_words=None):
        self.user_name = user_name
        self.used_words = used_words
        if self.used_words is None:
            self.used_words = []

    def __repr__(self):
        return f'Экземпляр класса "Player", который содержит в себе  {self.user_name} и {self.used_words}'

    def len_used_words(self):
        """Получение количества использованных слов."""
        return int(len(self.used_words))

    def add_used_word(self, user_word):
        """Добавление слова в использованные слова."""
        self.used_words.append(user_word)

    def check_used_word(self, user_word):
        """Проверка повторного ипсользования введенного слова в списке использованных слов."""
        if user_word in self.used_words:
            return True
