import numpy as np

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


def game_core_v3(number: int=1) -> int:
    """
       1. Устанавливаем любое random число
       2. Определяем минимальные и максимальные границы, которые, по умолчанию, равны интервалу угадывания
       3. В ходе выполнения работы корректируем минимальные и максимальные границы угадывания
       4. Значение переменной predict всегда принимает округленное в большую сторону значение на середине интервала допустимых границ

       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0
    predict = np.random.randint(1, 101)
    greater_num, smaller_num = 100, 0
    
    while number != predict:
        count += 1
        if number > predict:
            smaller_num = predict

        elif number < predict:
            greater_num = predict
        
        predict = np.ceil ((smaller_num + greater_num)/2)
        
    # Ваш код заканчивается здесь

    return count

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
