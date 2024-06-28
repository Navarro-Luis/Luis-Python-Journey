#accessing the global variable within a function

total =0

def count():
    global total
    total += 1
    return total

print(count())

