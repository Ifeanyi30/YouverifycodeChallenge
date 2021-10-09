def urlify(word):
    """Function to replace whitespace within a text with %20"""

    # strip whitespace from both sides of the text
    # replace the whitespace within the text with %20
    # then return the percentage encoded text.
    return (word.strip()).replace(" ", "%20")
