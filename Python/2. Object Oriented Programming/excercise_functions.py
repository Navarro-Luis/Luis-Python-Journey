#my answer: which works
def highest_even(li):
    even_numbers = []
    for number in li:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return max(even_numbers)
            

print(highest_even([10,2,3,4,8,11]))

#course answer:
def highest_even(li):
    even_numbers = []
    for number in li:
        if number % 2 == 0:
            even_numbers.append(number)
    return max(even_numbers)

print(highest_even([10,2,3,4,8,1]))