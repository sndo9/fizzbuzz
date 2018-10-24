
def fizzbuzz(start, finish):
    for i in range(start, finish + 1):
        output = ""
        if i % 3 != 0 and i % 5 != 0:
            output += str(i)
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        print(output)


fizzbuzz(1, 16)
