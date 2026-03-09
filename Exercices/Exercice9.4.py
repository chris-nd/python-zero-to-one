def filter_word_size(liste):
    return [word for word in liste if len(word) > 5]

print(filter_word_size(["chat", "python", "code", "programmation", "test"]))