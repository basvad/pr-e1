from enum import Enum
import time
import random
#список слов
WORDS_LIST = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
MAX_AMOUNT_OF_ATTEMPS = 4

class Result(Enum):
    FAIL = 0
    WIN = 1
    CONTINUE = -1
#функция случайного выбора слова
def choose_word(word_list):
    return random.choice(word_list)
#подсчет очков
def calculate_score(wrong_guesses):
    return max(MAX_AMOUNT_OF_ATTEMPS - wrong_guesses, 0)

#
class Game():
    # нициализация
    def __init__(self):
        #присваиваем ответ
        self.answer = choose_word(WORDS_LIST)
        self.guess_count = 0
        self.guessed_letters = []
    #попытка отгадать букву
    def guess(self, letter):
        #Возвращает флаг, указывающий на то, содержит ли строка только буквы
        if not letter.isalpha():
            raise ValueError
        #если получили не продолжение 
        if self.get_result() != Result.CONTINUE:
            raise ValueError
        #добавляем в список букву
        self.guessed_letters.append(letter)
        #если буква есть в ответе возвращаем true
        if letter.lower() in self.answer:
            return True
        #если нет, то увеличиваем счетчик попыток на 1 и возвращаем false
        else:
            self.guess_count += 1
            return False
    #Проходим по буквам в ответе и вписываем вместо угаданных правильные буквы, а вместо не угаданных — прочерки.
    def get_current_state(self):
        current_state = []
        for i in self.answer:
            if i in self.guessed_letters:
                current_state.append(i)
            else:
                current_state.append('_')
        return ''.join(current_state)
    #проверяем количество ошибок. Угадали ли мы слово?
    def get_result(self):
        #если количесвто попыток больше, то возвращаем FAIL
        if self.guess_count >= MAX_AMOUNT_OF_ATTEMPS:
            return Result.FAIL
        #если все буквы отгаданы, возвращаем WIN
        elif self.answer == self.get_current_state():
            return Result.WIN
        #продолжаем
        else:
            return Result.CONTINUE
#создание игры
def create_game():
    game = Game()
    return game
#проверка следующего шага
def next_step(result):
    if result == Result.WIN:
        print("Победа")
    elif result == Result.FAIL:
        print("Поражение")
    else:
        time.sleep(0.1)
        return True

#игра
def cli_gameplay():
    print("Я загадал слово. Вы должны угадать букву за буквой")
    print("Будьте осторожны, у вас всего 4 неудачных попытки")
    game = Game()
    print(game.get_current_state())
    while True:
        letter = input()
        try:
            game.guess(letter)
        except ValueError:
            print("Используйте буквы")
        print(game.get_current_state())
        result = game.get_result()
        do_continue = next_step(result)
        if not do_continue:
            raise StopIteration

if __name__ == '__main__': 
    while True: 
        cli_gameplay()