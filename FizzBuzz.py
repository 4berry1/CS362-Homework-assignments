def fizzbuzz(a):
    b = ""
    if (a % 3 == 0):
        b = "Fizz"
    if (a % 5 == 0):
        b += "Buzz"
    if (b == ""):
        b = a

    return b