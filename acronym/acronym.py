def abbreviate(words):
    array_of_words = words.replace('_', ' ').replace(
        '-', ' ').split(' ')
    acronym = ""
    for word in array_of_words:
        evaluated_word = word.strip()
        if (evaluated_word != ''):
            acronym = acronym + evaluated_word[0:1]
    return acronym.upper()
