def find_best_threshold_hard_exclusive(file_path, chunk_size=10000):
    # Шаг 1: Инициализация переменных
    min_errors = float('inf')
    best_t = None
    count_0_total, count_1_total = 0, 0

    # Шаг 2: Считаем общее количество классов (0 и 1)
    with open(file_path, 'r') as file:
        for line in file:
            _, y = map(int, line.split())
            if y == 0:
                count_0_total += 1
            else:
                count_1_total += 1

    # Шаг 3: Пакетная обработка
    left_0, left_1 = 0, 0
    with open(file_path, 'r') as file:
        data_chunk = []
        for line in file:
            x, y = map(int, line.split())
            data_chunk.append((x, y))

            # Когда накопили chunk_size строк, обрабатываем пакет
            if len(data_chunk) >= chunk_size:
                data_chunk.sort()  # Сортируем пакет по x
                for i in range(len(data_chunk)):
                    x, y = data_chunk[i]

                    # Условие: пропускаем текущий порог t (не включаем в подсчёт)
                    if i < len(data_chunk) - 1 and data_chunk[i + 1][0] == x:
                        continue

                    # Подсчёт ошибок для текущего порога
                    errors_left = left_1  # Ошибки слева
                    errors_right = count_0_total - left_0  # Ошибки справа
                    total_errors = errors_left + errors_right

                    # Условие выбора минимального порога
                    if total_errors < min_errors or (total_errors == min_errors and (best_t is None or x < best_t)):
                        min_errors = total_errors
                        best_t = x

                    # Обновляем счётчики
                    if y == 0:
                        left_0 += 1
                    else:
                        left_1 += 1

                # Обнуляем текущий пакет
                data_chunk = []

        # Обработка оставшихся данных
        if data_chunk:
            data_chunk.sort()
            for i in range(len(data_chunk)):
                x, y = data_chunk[i]

                # Пропускаем текущий порог t
                if i < len(data_chunk) - 1 and data_chunk[i + 1][0] == x:
                    continue

                errors_left = left_1
                errors_right = count_0_total - left_0
                total_errors = errors_left + errors_right

                if total_errors < min_errors or (total_errors == min_errors and (best_t is None or x < best_t)):
                    min_errors = total_errors
                    best_t = x

                if y == 0:
                    left_0 += 1
                else:
                    left_1 += 1

    return best_t, min_errors

# Пример вызова
file_path = 'data_hard.txt'
best_t, min_errors = find_best_threshold_hard_exclusive(file_path)
print(best_t, min_errors)
