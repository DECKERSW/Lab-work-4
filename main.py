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
