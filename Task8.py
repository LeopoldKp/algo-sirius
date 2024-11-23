"""
Венгерский алгоритм — метод для решения задач комбинаторной оптимизации, таких как задача о назначениях.
Алгоритм находит максимальное паросочетание в двудольных графах и минимизирует стоимость в задачах о назначениях.

Теоретическая оценка сложности:

    Временная сложность:
        O(n^3), где n — максимальное количество задач или исполнителей.

    Затраты по памяти:
        O(n^2) для хранения матрицы затрат.

Эта реализация использует матрицу смежности, где cost[i][j] представляет стоимость назначения задачи i исполнителю j.
"""

import numpy as np

def hungarian_algorithm(cost_matrix):
    # Количество задач и исполнителей
    n, m = cost_matrix.shape

    # Убедимся, что количество задач равно количеству исполнителей
    if n != m:
        raise ValueError("Количество задач должно быть равно количеству исполнителей.")

    # Шаг 1: Вычитаем минимальные элементы из строк
    for i in range(n):
        min_value = np.min(cost_matrix[i])  # Находим минимальное значение в строке
        cost_matrix[i] -= min_value  # Вычитаем его из всей строки

    # Шаг 2: Вычитаем минимальные элементы из столбцов
    for j in range(m):
        min_value = np.min(cost_matrix[:, j])  # Находим минимальное значение в столбце
        cost_matrix[:, j] -= min_value  # Вычитаем его из всего столбца

    # Создаем матрицу для отслеживания покрытых строк и столбцов
    covered_rows = np.zeros(n, dtype=bool)
    covered_cols = np.zeros(m, dtype=bool)

    # Шаг 3: Находим нулевые элементы и помечаем их
    zero_positions = []
    for i in range(n):
        for j in range(m):
            if cost_matrix[i, j] == 0 and not covered_rows[i] and not covered_cols[j]:
                zero_positions.append((i, j))  # Сохраняем позицию нуля
                covered_rows[i] = True  # Помечаем строку как покрытую
                covered_cols[j] = True  # Помечаем столбец как покрытый

    # Шаг 4: Алгоритм поиска максимального паросочетания в двудольном графе
    def find_matching():
        match_row = [-1] * n  # Массив для хранения соответствий строк
        match_col = [-1] * m  # Массив для хранения соответствий столбцов

        # Пробуем установить соответствия для нулевых позиций
        for i, j in zero_positions:
            if match_row[i] == -1 and match_col[j] == -1:
                match_row[i] = j  # Устанавливаем соответствие строки и столбца
                match_col[j] = i  # Устанавливаем соответствие столбца и строки

        return match_row, match_col

    match_row, match_col = find_matching()  # Начальное соответствие

    # Шаг 5: Проверяем, все ли задачи назначены
    while -1 in match_row:  # Пока есть незанятые задачи
        # Находим минимальное неназначенное значение
        min_uncovered = np.inf
        for i in range(n):
            for j in range(m):
                if not covered_rows[i] and not covered_cols[j]:
                    min_uncovered = min(min_uncovered, cost_matrix[i, j])

        # Обновляем матрицу
        for i in range(n):
            for j in range(m):
                if covered_rows[i] and covered_cols[j]:
                    cost_matrix[i, j] += min_uncovered  # Увеличиваем покрытые значения
                elif not covered_rows[i] and not covered_cols[j]:
                    cost_matrix[i, j] -= min_uncovered  # Уменьшаем непокрытые значения

        # Повторно находим нулевые позиции
        zero_positions = []
        covered_rows[:] = False  # Сбрасываем покрытые строки
        covered_cols[:] = False  # Сбрасываем покрытые столбцы
        for i in range(n):
            for j in range(m):
                if cost_matrix[i, j] == 0 and not covered_rows[i] and not covered_cols[j]:
                    zero_positions.append((i, j))  # Сохраняем позицию нуля
                    covered_rows[i] = True  # Помечаем строку как покрытую
                    covered_cols[j] = True  # Помечаем столбец как покрытый

        match_row, match_col = find_matching()  # Находим новое соответствие

    return match_row  # Возвращаем соответствия задачам

# Пример использования
if __name__ == "__main__":
    # Стоимость назначения задач исполнителям
    cost_matrix = np.array([[3, 4, 2, 8],
                             [1, 2, 4, 6],
                             [9, 8, 6, 4],
                             [5, 4, 3, 8]])

    assignments = hungarian_algorithm(cost_matrix)  # Запускаем алгоритм
    print("Назначения (задача -> исполнитель):")
    for task, worker in enumerate(assignments):
        print(f"Задача {task} назначена исполнителю {worker}")
