

def checkDriverAge(age=0):

    if age < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif age > 18:
        print("Powering On. Enjoy the ride!")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(92)
	
