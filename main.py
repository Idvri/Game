from data.utils import load_random_word
from data.classes import Player


# Главный код игры.
def main():
    input('Нажми Enter, чтобы начать игру...')
    player = Player(input('\nПора познакомиться. Укажи, пожалуйста, своё имя - '))
    word = load_random_word('https://api.npoint.io/bcd45a80626251861c2c')

    print(f'''\nПривет, {player.user_name}!!
Составь {word.len_sub_words()} слов из слова "{word.default_word.title()}"!
Слова должны быть не короче {len(min(word.sub_words))} букв.
Чтобы закончить игру, угадай все слова или напиши "stop".''')

    print('\nПоехали!')
    # Цикл, который будет работать пока кол-во угаданных игроком слов не сравняется с кол-ом слов из списка подслов.
    while player.len_used_words() != word.len_sub_words():
        user_answer = (input('\nВведи слово: ')).lower()

        # Условие, при котором можно остановить игру не отгдывая все слова.
        if user_answer == 'stop' or user_answer == 'стоп':
            break
        elif len(user_answer) < len(min(word.sub_words)):
            print('Слишком короткое слово. Попытайся ещё раз.')
            continue
        elif not word.check_word(user_answer):
            print('Неверно. Попытайся ещё раз.')
            continue
        elif player.check_used_word(user_answer):
            print('Это слово уже использовано. Попытайся ещё раз.')
            continue
        else:
            player.add_used_word(user_answer)
            print(f'Верно. Осталось отгадать {word.len_sub_words() - player.len_used_words()}.')

    # Вывод статистики игры.
    print(f'\nИгра завершена, кол-во угаданных слов: {player.len_used_words()}!')


main()
