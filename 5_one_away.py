def one_away(str1, str2):

    wrd_len_1 = len(str1)
    wrd_len_2 = len(str2)
    char_check = 0

    if not (abs(wrd_len_1 - wrd_len_2) >= 2):
        base_wrd = str1 if wrd_len_1 >= wrd_len_2 else str2
        edited = str2 if wrd_len_2 <= wrd_len_1 else str1

        for i in range(wrd_len_2):
            if edited[i] in base_wrd:
                char_check += 1
    else:
        return False

    if wrd_len_1 - 1 == char_check:
        return True
    return False


print(one_away("palfde", "pal"))
