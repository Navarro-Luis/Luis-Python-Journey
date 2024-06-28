# is_old = False
# is_licensed = True

# if is_old and is_licensed:

#     print('You are old enough to drive and you are licensed')


# # elif is_licensed:
# #     print('You can drive now!')


# else: 
#     print('You are not of age!!!')


# is_magician = False
# is_expert = False

# if is_magician and is_expert:
#     print('you are a master magician')

# if is_magician and not is_expert:
#     print('at least you are getting there!')

# if not is_magician:
#     print('You need magic powers')


#seif notes

#dictionary
user_info = {
    "alice":
      {
          "age": 25,
          "city": "New York"
          },
    "bob":
      {"age": 30,
       "city": "San Francisco"
       }
}

###print new York
# print(user_info['alice']['city'])

#sets

# array = [1,1,1,2,2,3,4,5,6]

# unique_numbers = set(array)
# print(array)
# print(unique_numbers)

# import array
# numbers = array.array('i', [1, 2, 3, 4, 5])
# print(numbers)

#lists
shopping_list = ["eggs", "milk", "bread", "butter"]
shopping_total = 0
wallet = 100
shopping_list_dollar_val = [10,5,5,10]

for i in shopping_list: 
    if i == 'eggs': 
        shopping_total = shopping_total+9
    

print(shopping_total)

