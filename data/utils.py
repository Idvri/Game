import requests
# Импорт ниже оформлен именно таким образом, чтобы его видел main.py при вызове функции из этого файла.
import data.classes
import json
import random


# Функция для получения случайного слова и списка его подслов со стороннего ресурса.
def load_random_word(words):
    response = requests.get(words)
    words_text = json.loads(response.text)
    random.shuffle(words_text)

    return data.classes.BasicWord(words_text[0]["word"], words_text[0]["subwords"])
