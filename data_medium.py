def find_best_threshold_fast(file_path):
    # Шаг 1: Считываем данные
    with open(file_path, 'r') as file:
        data = [tuple(map(int, line.split())) for line in file]

    # Шаг 2: Сортируем данные по x
    data.sort()

    # Шаг 3: Подсчитываем общее количество классов
    count_0 = sum(1 for _, y in data if y == 0)
    count_1 = sum(1 for _, y in data if y == 1)

    # Шаг 4: Инициализация переменных
    min_errors = float('inf')
    best_t = None
    left_0, left_1 = 0, 0

    # Шаг 5: Проходим по данным и считаем ошибки на каждом пороге
    for i in range(len(data)):
        x, y = data[i]

        # Обновляем нарастающие суммы
        if y == 0:
            left_0 += 1
        else:
            left_1 += 1

        if i < len(data) - 1:
            next_x = data[i + 1][0]
            t = (x + next_x) // 2 + (x + next_x // 2) % 2
        else:
            t = x  # Для последней точки берём её значение

        # Подсчёт ошибок
        errors_left = left_1  # Ошибки в левой части (1 остались слева от t)
        errors_right = count_0 - left_0  # Ошибки в правой части (0 остались справа от t)
        total_errors = errors_left + errors_right

        # Сохраняем порог, если нашли меньше ошибок, или выбираем минимальный индекс при равных ошибках
        if total_errors < min_errors or (total_errors == min_errors and (best_t is None or t < best_t)):
            min_errors = total_errors
            best_t = t

    return best_t, min_errors

file_path = 'data_medium.txt'
best_t, min_errors = find_best_threshold_fast(file_path)

print(best_t, min_errors)
