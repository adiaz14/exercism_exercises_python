def count_words(sentence):
    counting = {}
    group_of_words = sentence.replace('_', ' ').replace(
        '_', ' ').replace(',', ' ').split()
    for word in group_of_words:
        word = word.lower().strip("!&@$%^:,'.")
        if word == '':
            continue
        if word in counting:
            counting[word] += 1
        else:
            counting[word] = 1
    return counting
