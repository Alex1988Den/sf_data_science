import numpy as np


def random_predict(number: int = 1) -> int:
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
# Предполагаемое число выбирается случайным образом
        if number == predict_number:
            break  # Выход из цикла, если угадали число
    return count


def game_core_v2(number: int = 1) -> int:
    count = 0
    predict = np.random.randint(1, 101)
# Устанавливаем случайное число в качестве предполагаемого
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
# Увеличиваем предполагаемое число, если загаданное число больше
        elif number < predict:
            predict -= 1
# Уменьшаем предполагаемое число, если загаданное число меньше
    return count


def score_game(game_core) -> int:
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (10000))
# Создаем массив случайных чисел

    for number in random_array:
        count_ls.append(game_core(number))
# Запускаем алгоритм для каждого числа в массиве

    score = int(np.mean(count_ls))  # Вычисляем среднее количество попыток
    print(f"Your algorithm guesses in an average of {score} attempts")


def game_core_v3(number: int = 1) -> int:
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict = (low + high) // 2
# Предполагаемое число - среднее между нижней и верхней границами

        if predict == number:
            break  # Выход из цикла, если угадали число
        elif predict < number:
            low = predict + 1  # Сдвигаем нижнюю границу поиска
        else:
            high = predict - 1  # Сдвигаем верхнюю границу поиска

    return count

print('Run benchmarking for random_predict: ', end = '')
score_game(random_predict)

print('Run benchmarking for game_core_v2: ', end = '')
score_game(game_core_v2)

print('Run benchmarking for game_core_v3: ', end = '')
score_game(game_core_v3)
