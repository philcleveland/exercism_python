def convert(number):
    x = ""
    if number%3 == 0:
        x = x + "Pling"
    if number%5 == 0:
        x = x + "Plang"
    if number%7 == 0:
        x = x + "Plong"
    if x == "":
        x = str(number)
    return x