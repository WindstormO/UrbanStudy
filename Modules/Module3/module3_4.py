def single_root_words(root_word, *other_words):
    """Функция, определяющая однокоренные слова"""
    same_words = []
    print(f"root_word:{root_word} , other_words: {other_words}")
    for words in range(len(other_words)):
        if root_word.lower() in other_words[words].lower() or other_words[words].lower() in root_word.lower():
            same_words.append(other_words[words])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
