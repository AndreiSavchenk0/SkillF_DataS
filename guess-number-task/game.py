"""Игра угадай число"""

import numpy as np

def random_predict(number: int = 1) -> int:
    print(number)
    """Рандомно угадываем число
    Args:
        number(int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    min = 1 # нижняя граница
    max = 100 # верхняя граница
    predict_number = np.random.randint(1, 101)  # предполагаемое число, начинаем с рандома
    while True:
        count += 1
        if number > predict_number:
            min = predict_number
            predict_number = max - (max - min)//2
        elif number < predict_number:
            max = predict_number
            predict_number = max//2
        else:
            break  # выход из цикла если угадали
        
    return count

print(random_predict(1))
