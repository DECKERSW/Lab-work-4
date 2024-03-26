# Програмний код для обробки тексту
#Кот Михайло
# Введення тексту від першого студента (первісний текст)
input_text = "Тут розміщений текст, який включає в себе до 100 слів."

# Виведення оригінального тексту
print("Оригінальний текст:")
print(input_text)

# Функція для розбиття тексту на слова
def split_into_words(text):
    result = text.split()
    print("\nТекст після розбиття на слова:")
    print(result)
    return result

# Функція для перетворення тексту в нижній регістр
def to_lowercase(text):
    result = text.lower()
    print("\nТекст у нижньому регістрі:")
    print(result)
    return result

# Функція для визначення кількості слів у тексті
def count_words(text):
    words = split_into_words(text)
    result = len(words)
    print("\nКількість слів у тексті:", result)
    return result

# Застосовуємо функції до вхідного тексту
lowercase_text = to_lowercase(input_text)
word_count = count_words(input_text)


# Баженов Данило

#Функція для перетворення першої літери кожного слова на велику
def title_first_letter(text):
    w_up = text.title()
    print("After\nВ тексті перші літери кожного слова великі\n\n ", w_up)
    return w_up

#Функція для знаходження унікальних символів у тексті
def find_unique_words(text):
    words = text.split()  # Розбиваємо текст на слова
    word_counts = {}  # Створюємо словник для підрахунку кількості кожного слова
    unique_words = []  # Список для зберігання унікальних слів

    # Підрахунок кількості кожного слова
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Додавання унікальних слів до списку
    for word, count in word_counts.items():
        if count == 1:
            unique_words.append(word.lower())  # Перетворюємо слово на нижній регістр перед додаванням

    return unique_words
#Функція для обернення тексту у  зворотному порядку
def reverse_text(text):
    reversed_text = text[::-1]  # Обертаємо текст у зворотному порядку
    return reversed_text

#функції до вхідного тексту
#input_text = title_first_letter(input_text)  # Виправлено
#input_text = find_unique_words(input_text)
#input_text = reverse_text(input_text)