def str_compressed(string):
    """String Compression

    Strings are compressed with the length of consecutive letters
    encoded next to each.

    Arguments:
    ---------
    strings: The word to be compressed (String)

    Returns:
    -------
    A string of compressed values eg: 'a2b3c5', or the word itself
    if not compressable.
    """

    string = str(string)

    # return None if the string contains other character types
    if not string.isalnum():
        print("string must be alphanumeric")
        return
    string_mock = string + "\n"

    str_len = len(string_mock)
    result_str = ""
    result_dict = {}

    # parameters for looping and comparison for string chars
    flag = 0
    current_char = string[0]
    count = 0

    while flag < str_len:
        if current_char == string_mock[flag]:
            count += 1
            flag += 1
        else:
            result_str += current_char + str(count)
            current_char = string_mock[flag]
            count = 1
            flag += 1

    # populate the result dictionary
    for i in range(0, len(result_str), 2):
        result_dict[result_str[i]] = int(result_str[i + 1])

    if len(result_dict) == sum(result_dict.values()) or len(string) < 2:
        return string
    else:
        return result_str

