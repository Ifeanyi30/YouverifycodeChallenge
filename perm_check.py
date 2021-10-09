class MyStr:
    """Locally created string class

    This is a string template with methods to check if two string
    are permutations of each other and a character sorting method

    Arguments:
    value: (String)
    other: (object) instance of the MyStr class

    Methods:
    -------
    sort_wrd_char: sort and return string value
    is_perm: checks for words permutation (Boolean)
    """

    def __init__(self, value):
        self.value = str(value)

    def sort_wrd_char(self, value):

        return "".join(sorted(value))

    def is_perm(self, other):
        if len(self.value) != len(other.value):
            return False
        else:
            # sort both words alphabetically for easy comparison
            first_str = self.sort_wrd_char(self.value)
            second_str = self.sort_wrd_char(other.value)

            # check if both string values are not equal
            if first_str != second_str:
                return False
            return True
