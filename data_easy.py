with open('data_medium.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

min_errors = float('inf')
best_t = None

for t in [point[0] for point in data]:
    errors = sum(1 for x, y in data if (x < t and y == 1) or (x >= t and y == 0))
    # Условие обновления:строго меньшее количество ошибок или минимальный индекс при равных ошибках
    if errors < min_errors or (errors == min_errors and (best_t is None or t < best_t)):
        min_errors = errors
        best_t = t

print(best_t, min_errors)


