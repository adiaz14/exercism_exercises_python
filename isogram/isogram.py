def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').upper()
    string_list = list(string)
    for value in (string_list):
        count = 0
        for evaluating_value in (string_list):
            if(value == evaluating_value):
                count = count + 1
        if(count > 1):
            return False
    return True
