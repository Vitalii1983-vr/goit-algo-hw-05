def binary_search(arr, x):
    # Ініціалізація змінних
    low = 0  # Початковий індекс діапазону пошуку
    high = len(arr) - 1  # Кінцевий індекс діапазону пошуку
    iterations = 0  # Лічильник кількості ітерацій
    upper_bound = None  # Змінна для збереження найменшого елемента, більшого або рівного x

    # Цикл виконується, поки діапазон пошуку не звузиться до нуля
    while low <= high:
        iterations += 1  # Збільшення лічильника ітерацій на кожному кроці
        mid = (high + low) // 2  # Обчислення середнього індексу поточного діапазону

        # Якщо середній елемент менший за шукане значення, зсуваємо нижню межу вгору
        if arr[mid] < x:
            low = mid + 1
        # Якщо середній елемент більший або дорівнює шуканому значенню, зсуваємо верхню межу вниз
        else:
            if upper_bound is None or arr[mid] < upper_bound:
                upper_bound = arr[mid]
            high = mid - 1

    # Повертаємо кількість ітерацій та верхню межу як кортеж
    return (iterations, upper_bound)

# Використання функції
arr = [0.1, 1.5, 2.3, 3.8, 4.5, 5.9, 7.2, 8.1]  # Відсортований масив з дробовими числами
x = 4.0  # Шукане значення

# Виклик функції двійкового пошуку та збереження результату
result = binary_search(arr, x)

# Виведення результату
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")