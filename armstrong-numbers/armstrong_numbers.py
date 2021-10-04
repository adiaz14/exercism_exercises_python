def is_armstrong_number(number):
    sum = 0
    temp = number
    exp = len(str(number))
    digit = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** exp
        temp //= 10
    if number == sum:
        return True
    else:
        return False
