def is_unique(word):
    word_len = len(word)
    for char in word:
        char_index = word.index(char)
        if char_index == word_len - 1:
            return True
        else:
            result = word.find(char, char_index + 1)
            if result != -1:
                return False
                