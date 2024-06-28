#error handling

#reads: I want you to try  this code and if error happens print this. otherwise print thank you
while True:
    try:
        age = int(input('What is your age? ')) #make this an int so only receive integers and error if not

        print(age)
        10/age
    except ValueError: #can make the except block accept only a certain error!
        print("Please enter number")
    except ZeroDivisionError: 
        print("Please enter a non-zero number")
    else:
        print('thank you!')
        break