'''
Задание № 4:

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

'''

import random
from tqdm import tqdm ### для простоты ожидания поиска расстановок, чтобы использовать строку прогресса.

def is_valid_queen_arrangement(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if (
                queens[i][0] == queens[j][0] or # Проверка атаки по горизонтали
                queens[i][1] == queens[j][1] or # Проверка атаки по вертикали
                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]) # Проверка атаки по диагонали
            ):
                return False
    return True

def generate_random_queen_arrangement():
    queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return queens

def find_successful_placements(num_placements=4):
    print("Работает функция поиска расстановок...")
    successful_placements = []
    attempts = 0
    
    with tqdm(total=num_placements) as pbar: # работа строки прогресса
        while len(successful_placements) < num_placements:
            queens = generate_random_queen_arrangement()
            if is_valid_queen_arrangement(queens):
                successful_placements.append(queens)
                pbar.update(1)  # обновление строки прогресса
            attempts += 1

    return successful_placements

if __name__ == "__main__":
    num_successful_placements = 4
    successful_placements = find_successful_placements(num_successful_placements)
    
    for i, placement in enumerate(successful_placements):
        print(f"Правильная расстановка № {i + 1}:")
        for queen in placement:
            print(f"Ферзь на поле ({queen[0]}, {queen[1]})")
        print()
