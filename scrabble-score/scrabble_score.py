def score(word):
    score = 0
    letter_array = list(word.upper())
    array_values_one = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    array_values_two = ['D', 'G']
    array_values_three = ['B', 'C', 'M', 'P']
    array_values_four = ['F', 'H', 'V', 'W', 'Y']
    array_values_five = ['K']
    array_values_six = ['J', 'X']
    for letter in letter_array:
        if letter in array_values_one:
            score = score + 1
        elif letter in array_values_two:
            score = score + 2
        elif letter in array_values_three:
            score = score + 3
        elif letter in array_values_four:
            score = score + 4
        elif letter in array_values_five:
            score = score + 5
        elif letter in array_values_six:
            score = score + 8
        else:
            score = score + 10
    return score
