def year(a):
    if (a % 100 == 0):
        return "{b} is not a leap year".format(b = a)
    elif (a % 4 == 0):
        return "{b} is a leap year".format(b = a)
    return "{b} is not a leap year".format(b = a)
