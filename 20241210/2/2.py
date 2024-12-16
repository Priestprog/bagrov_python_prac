import asyncio
import random

# Сопрограмма для слияния двух отсортированных отрезков
async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())  # Ждем сортировки подотрезков
    i, j, k = start, middle, start

    # Слияние двух подотрезков
    while i < middle and j < finish:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    # Копирование оставшихся элементов из левого подотрезка
    while i < middle:
        B[k] = A[i]
        i += 1
        k += 1

    # Копирование оставшихся элементов из правого подотрезка
    while j < finish:
        B[k] = A[j]
        j += 1
        k += 1

    event_out.set()  # Сообщаем о завершении задачи

# Планирование задач сортировки слиянием
async def mtasks(A):
    copy_of_A = A.copy()
    N = len(copy_of_A)
    B = [0] * N  # Вспомогательный массив
    tasks = []
    current_array = copy_of_A  # Сортируемые массивы будут чередоваться
    next_array = B

    # Создаем события для синхронизации
    events = [[asyncio.Event() for _ in range((N + (1 << level) - 1) // (1 << level))]
              for level in range((N - 1).bit_length() + 1)]

    # Этапы слияния отрезков длины 1, 2, 4 и т.д.
    step = 1
    level = 0
    while step < N:
        for start in range(0, N, 2 * step):
            middle = min(start + step, N)
            finish = min(start + 2 * step, N)

            # События для текущего уровня
            event_in1 = events[level][start // step]
            event_in2 = events[level][middle // step if middle < N else (start // step)]
            event_out = events[level + 1][start // (2 * step)]

            # Создаем задачу для слияния
            task = merge(current_array, next_array, start, middle, finish, event_in1, event_in2, event_out)
            tasks.append(task)

        # Меняем местами текущий и следующий массивы
        current_array, next_array = next_array, current_array
        step *= 2
        level += 1

    # Сигнализируем, что исходные единичные отрезки отсортированы
    for i in range(len(events[0])):
        events[0][i].set()

    # Убедимся, что результат находится в массиве A
    if current_array is not copy_of_A:
        copy_of_A[:] = current_array[:]

    # Возвращаем и отсортированные задачи, и результат в B
    return tasks, current_array


import sys
exec(sys.stdin.read())
