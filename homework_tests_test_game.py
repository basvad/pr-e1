import pytest
from homework_app import choose_word, WORDS_LIST, \
calculate_score, create_game, MAX_AMOUNT_OF_ATTEMPS, Result, next_step

#тест случайного выбора слова
def test_choose_word():
    #выбрали слово
    random_word = choose_word(WORDS_LIST)
    #проверили, что оно находится в списке
    assert random_word in WORDS_LIST

#тест подсчета очков
def test_calcualte_score_positive():
    #присвоили передачей 1 (из max=4 вычли 1)
    score = calculate_score(1)
    #сравнили
    assert score == 3

#проверка на передачу занчения больше макс
def test_calcualte_score_negative():
    #присвоили макс (-1,0)
    score = calculate_score(5)
    #сравнили с максимальным
    assert score == 0

#тест создания игры
def test_create_game():
    game = create_game()
    #проверка наличия ответа в списке вариантов
    assert game.answer in WORDS_LIST
    #проверка счетчика 
    assert game.guess_count == 0
    #проверка на пустототу списка букв
    assert game.guessed_letters == []

#проверка определения не букв
def test_guess_not_a_letter():
    game = create_game()
    with pytest.raises(ValueError):
        #передали число
        game.guess("1")

#проверка окончания игры
def test_guess_game_over():
    game = create_game()
    #присвоили макс знач + 1
    game.guess_count = MAX_AMOUNT_OF_ATTEMPS + 1
    with pytest.raises(ValueError):
        #пробуем передать еще одну букву
        game.guess("a")

# проверка успешного нахождения  
def test_guess_success():
    #создали игру
    game = create_game()
    #вытащили ответ
    answer = game.answer
    #передали первую букву ответа
    result = game.guess(answer[0])
    #проверяем результат true or false
    assert result
    # проверяем что счетчик не изменился
    assert game.guess_count == 0 
    # проверяем что буква попала в список букв
    assert answer[0] in game.guessed_letters
    # проверяем текущее состояние
    assert game.get_current_state().startswith(answer[0])

#проверка отрицательно сценария
def test_guess_not_success():
    game = create_game()
    result = game.guess('d')
    assert not result
    assert game.guess_count == 1
    assert 'd' in game.guessed_letters
    assert game.get_current_state() == '_'*len(game.answer)

#параметризация максимальное значение, максимальное значение + 1
# проверка на окончание игры
@pytest.mark.parametrize("attempts_number", [MAX_AMOUNT_OF_ATTEMPS, MAX_AMOUNT_OF_ATTEMPS+1])
def test_get_result_fail(attempts_number):
    game = create_game()
    game.guess_count = attempts_number 
    assert game.get_result() == Result.FAIL

#параметризация 0, максимальное значение - 1
#тест на продолжение игры
@pytest.mark.parametrize("attempts_number", [0, MAX_AMOUNT_OF_ATTEMPS - 1])
def test_get_result_continue(attempts_number):
    game = create_game()
    game.guess_count = attempts_number 
    assert game.get_result() == Result.CONTINUE

#параметризация 0, максимальное значение - 1
#тест на проверку
@pytest.mark.parametrize("attempts_number", [0, MAX_AMOUNT_OF_ATTEMPS - 1])
def test_get_result_win(attempts_number):
    game = create_game()
    game.guess_count = attempts_number 
    answer = game.answer
    #передаем сразу правильный ответ
    game.guessed_letters = list(answer
    assert game.get_result() == Result.WIN
#параметризация по результатам выигрыш, проигрыш
#тест отстутсвия следующего шага
@pytest.mark.parametrize("result", [Result.WIN, Result.FAIL])
def test_no_next_step(result):
    next_step_needed = next_step(result)
    assert not next_step_needed
#тест наличия следующего шага
def test_next_step():
    result = Result.CONTINUE
    next_step_needed = next_step(result)
    assert next_step_needed

    
    

