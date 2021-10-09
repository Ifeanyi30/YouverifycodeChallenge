def is_unique(word):
    """Checks for the uniqueness of characters in a word

    The function return true if all characters in the word
    given is unique and false if not

    Arguments:
    ---------
    word: the string parameter to be checked

    Returns:
    -------
    Returns a boolean type of either True or False
    """
    unique_char = []

    for char in word:
        if char not in unique_char:
            unique_char.append(char)
        else:
            return False
    return True
