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
    char_list = [i for i in word.lower()]

    unique_char = set(char_list)

    if len(unique_char) == len(char_list):
        return True
    return False


print(is_unique("Eagle"))
