def is_armstrong_number(number):
    number_as_string = str(number)
    num_digits = len(number_as_string)
    sum = 0
    for i in number_as_string:
        sum += int(i)**num_digits
    return sum == number
