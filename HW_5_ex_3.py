import gdown  # Імпорт бібліотеки для завантаження файлів з Google Drive
import timeit  # Імпорт бібліотеки для вимірювання часу виконання коду
import pandas as pd  # Імпорт бібліотеки для роботи з таблицями
from collections import defaultdict  # Імпорт defaultdict для створення таблиці зміщень

# Завантаження файлів з Google Drive за допомогою бібліотеки gdown
url1 = 'https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
url2 = 'https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'

# Завантаження першої статті
gdown.download(url1, 'article1.txt', quiet=False)
# Завантаження другої статті
gdown.download(url2, 'article2.txt', quiet=False)

# Читання текстових файлів
# Відкриваємо файл article1.txt для читання у режимі 'r' (read) з кодуванням 'ISO-8859-1'
with open('article1.txt', 'r', encoding='ISO-8859-1') as file:
    text1 = file.read()  # Читаємо вміст файлу у змінну text1

# Відкриваємо файл article2.txt для читання у режимі 'r' (read) з кодуванням 'ISO-8859-1'
with open('article2.txt', 'r', encoding='ISO-8859-1') as file:
    text2 = file.read()  # Читаємо вміст файлу у змінну text2

# Підрядки для пошуку
existing_substring = 'алгоритм'  # Підрядок, який існує у текстах
non_existing_substring = 'немає такого підрядка'  # Підрядок, якого немає у текстах

# Реалізація алгоритмів

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)  # Довжина підрядка (шаблону)
    n = len(text)  # Довжина тексту

    if m == 0:
        return 0  # Якщо підрядок порожній, повертаємо 0

    # Створення таблиці зміщень для символів у шаблоні
    skip = defaultdict(lambda: m)
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1

    k = m - 1  # Індекс у тексті, з якого починається порівняння
    while k < n:
        j = m - 1  # Індекс у шаблоні
        i = k  # Поточний індекс у тексті
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return k - m + 1  # Повертаємо початковий індекс знайденого підрядка
        k += skip[text[k]]  # Зміщення на наступний індекс для порівняння

    return -1  # Якщо підрядок не знайдено, повертаємо -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    m = len(pattern)  # Довжина підрядка (шаблону)
    n = len(text)  # Довжина тексту

    if m == 0:
        return 0  # Якщо підрядок порожній, повертаємо 0

    # Створення таблиці префіксів для шаблону
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)

    i = 0  # Індекс у тексті
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j  # Повертаємо початковий індекс знайденого підрядка
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1  # Якщо підрядок не знайдено, повертаємо -1

# Функція для створення таблиці префіксів (LPS - longest prefix suffix)
def compute_lps_array(pattern, m, lps):
    length = 0  # Довжина попереднього найдовшого префікса
    lps[0] = 0  # LPS для першого символу завжди 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, d=256, q=101):
    m = len(pattern)  # Довжина підрядка (шаблону)
    n = len(text)  # Довжина тексту
    p = 0  # Хеш значення для підрядка
    t = 0  # Хеш значення для тексту
    h = 1

    if m == 0:
        return 0  # Якщо підрядок порожній, повертаємо 0

    # Обчислення h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Обчислення початкового хеша підрядка і першого вікна тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Переміщення підрядка по тексту
    for i in range(n - m + 1):
        if p == t:  # Якщо хеші співпадають, перевіряємо символи
            if text[i:i + m] == pattern:
                return i  # Повертаємо початковий індекс знайденого підрядка

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1  # Якщо підрядок не знайдено, повертаємо -1

# Функція для вимірювання часу виконання алгоритму
def measure_time(algorithm, text, pattern):
    timer = timeit.Timer(lambda: algorithm(text, pattern))  # Створення таймера для вимірювання часу
    return timer.timeit(number=1000)  # Вимірювання часу виконання алгоритму 1000 разів

# Вимірювання часу для кожного алгоритму і тексту
algorithms = {
    'Boyer-Moore': boyer_moore,
    'KMP': kmp_search,
    'Rabin-Karp': rabin_karp
}

results = {}  # Словник для зберігання результатів

for name, algorithm in algorithms.items():
    results[name] = {
        'article1_existing': measure_time(algorithm, text1, existing_substring),
        'article1_non_existing': measure_time(algorithm, text1, non_existing_substring),
        'article2_existing': measure_time(algorithm, text2, existing_substring),
        'article2_non_existing': measure_time(algorithm, text2, non_existing_substring)
    }

# Виведення результатів
results_df = pd.DataFrame(results).T

# Виводимо результати у вигляді таблиці з додатковою інформацією
print("\nРезультати вимірювання часу виконання алгоритмів пошуку підрядка:\n")
print(results_df.to_string(index=True))

# Виведення найшвидшого алгоритму для кожного випадку
print("\nНайшвидший алгоритм для кожного випадку:\n")
for column in results_df.columns:
    min_value = results_df[column].min()
    fastest_algorithm = results_df[results_df[column] == min_value].index[0]
    print(f"Для {column.replace('_', ' ')}: {fastest_algorithm} з часом {min_value:.8f} секунд")

# Виведення загального найшвидшого алгоритму
overall_fastest_algorithm = results_df.sum(axis=1).idxmin()
overall_min_time = results_df.sum(axis=1).min()
print(f"\nЗагальний найшвидший алгоритм: {overall_fastest_algorithm} з сумарним часом {overall_min_time:.8f} секунд")
