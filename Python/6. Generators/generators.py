# a generator allows us to use a keywork yeild. range() is a generator

# range(100)
# list(range(100))


def generator_function(num):
    for i in range(num):
        yield i*2

g = generator_function(100)

print(next(g))



# for item in generator_function(1000):
#     print(item)
