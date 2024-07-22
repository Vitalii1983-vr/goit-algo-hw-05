class HashTable:
    def __init__(self, size):
        # Ініціалізація хеш-таблиці з заданим розміром.
        # Створює порожній список для кожного слота в хеш-таблиці.
        self.size = size  # Зберігаємо розмір хеш-таблиці.
        self.table = [[] for _ in range(self.size)]  # Створюємо список списків для зберігання пар ключ-значення.

    def hash_function(self, key):
        # Хеш-функція для перетворення ключа в індекс хеш-таблиці.
        return hash(key) % self.size  # Використовуємо вбудовану функцію hash() та беремо залишок від ділення на розмір таблиці.

    def insert(self, key, value):
        # Метод для вставки нової пари ключ-значення в хеш-таблицю.
        key_hash = self.hash_function(key)  # Обчислюємо хеш ключа.
        key_value = [key, value]  # Створюємо пару ключ-значення.

        if self.table[key_hash] is None:
            # Якщо у хеш-таблиці за цим індексом ще немає записів, створюємо новий список з парою ключ-значення.
            self.table[key_hash] = list([key_value])
            return True  # Повертаємо True, щоб показати, що вставка була успішною.
        else:
            # Якщо за цим індексом вже є записи, перевіряємо, чи є ключ вже у списку.
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    # Якщо ключ вже існує, оновлюємо його значення.
                    pair[1] = value
                    return True  # Повертаємо True, щоб показати, що оновлення було успішним.
            # Якщо ключ не знайдено, додаємо нову пару ключ-значення до списку.
            self.table[key_hash].append(key_value)
            return True  # Повертаємо True, щоб показати, що вставка була успішною.

    def get(self, key):
        # Метод для отримання значення за заданим ключем.
        key_hash = self.hash_function(key)  # Обчислюємо хеш ключа.
        if self.table[key_hash] is not None:
            # Якщо за цим індексом є записи, шукаємо ключ у списку.
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]  # Повертаємо значення, якщо ключ знайдено.
        return None  # Повертаємо None, якщо ключ не знайдено.

    def delete(self, key):
        # Метод для видалення пари ключ-значення з хеш-таблиці.
        key_hash = self.hash_function(key)  # Обчислюємо хеш ключа.
        if self.table[key_hash] is not None:
            # Якщо за цим індексом є записи, шукаємо ключ у списку.
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    # Якщо ключ знайдено, видаляємо пару ключ-значення зі списку.
                    self.table[key_hash].pop(i)
                    return True  # Повертаємо True, щоб показати, що видалення було успішним.
        return False  # Повертаємо False, якщо ключ не знайдено.

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)  # Створюємо хеш-таблицю з 5 слотами.
H.insert("apple", 10)  # Вставляємо пару ключ-значення ("apple", 10).
H.insert("orange", 20)  # Вставляємо пару ключ-значення ("orange", 20).
H.insert("banana", 30)  # Вставляємо пару ключ-значення ("banana", 30).

print(H.get("apple"))   # Виводимо значення за ключем "apple", очікується 10.
print(H.get("orange"))  # Виводимо значення за ключем "orange", очікується 20.
print(H.get("banana"))  # Виводимо значення за ключем "banana", очікується 30.

H.delete("apple")  # Видаляємо пару ключ-значення з ключем "apple".
print(H.get("apple"))   # Виводимо значення за ключем "apple", очікується None, оскільки ключ було видалено.
