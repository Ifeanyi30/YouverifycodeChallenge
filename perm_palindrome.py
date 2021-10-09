from string_compression import str_compressed


def list_split(mylist, start, length, step):

    return mylist[start:length:step]


def sort_wrd_char(value):

    return "".join(sorted(value))


def perm_palindrome(string):
    """Permutation Palindrome

    This function check if any permutation of rearrangement of a
    word is a palindrome

    Arguments:
    ---------
    string: The word to be checked (String)

    Return:
    ------
    It returns a Boolean value, True if Palindrome is found or false if not
    """

    string_sorted = sort_wrd_char(string).strip()

    wrd_len = len(string_sorted)
    even_count = 0
    even = 0
    odd = 0

    if wrd_len > 2:
        compressed_wrd = str_compressed(string_sorted)

        com_list = [i for i in compressed_wrd]
        char_freq = list_split(com_list, 1, len(com_list), 2)

        if not all(val.isdigit() for val in char_freq):
            return False

        for item in char_freq:
            if int(item) % 2 == 0:
                even = int(item)
                even_count += 1
            else:
                odd = int(item)

        return even_count * even == wrd_len or ((even_count * even) + odd == wrd_len)
    else:
        return False


print(perm_palindrome("tac"))
