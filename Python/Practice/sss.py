'''
Если длина слова больше 5 символов, оставить его без изменений. Если длина слова от 3 до 5 символов,
заменить слово на 'medium'. Если длина слова меньше 3 символов, заменить его на 'short'.
'''
words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
words_new = [word if len(word) > 5 else 'short' if len(word) < 3 else 'medium' for word in words]
print(words_new)