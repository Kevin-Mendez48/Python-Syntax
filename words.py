def print_upper_words(words):
    """Print each word in uppercase on a separate line."""
    for word in words:
        print(word.upper())

def print_words_starting_with_e(words):
    """Print words that start with 'e' (case insensitive)."""
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())

def print_words_starting_with_letters(words, must_start_with):
    """Print words that start with any letter in must_start_with (case insensitive)."""
    for word in words:
        if any(word.lower().startswith(letter) for letter in must_start_with):
            print(word.upper())
