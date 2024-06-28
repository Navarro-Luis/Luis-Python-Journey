# for number in (2,3,4,5,6,7,8,9,10,'J','Q','K','A'):
#     for suit in ('s','c','h','d'):
#         print(number,suit)

##ask seif how I might put this into an array or something

# luis = {
#     'age': 25,
#     'hair_color': 'black',
#     'weight': 155
# }

# for key,value in luis.items():
#     print(key,"=" ,value)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for item in my_list:
#     counter = counter +item
# print(counter)

# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'index of 50 is {i}')


##While loops

# i=0
# while i<50
# print(i)
# i+=1

##PICTURE PROGRAM
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

row=0
fill = 'A'
empty = ' '

while row<len(picture):
    for item in picture[row]:
        if item:
            print(fill, end = "")
        else:
            print(empty,end = "")
    print("")
    row+=1