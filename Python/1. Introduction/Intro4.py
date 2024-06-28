birth_year = input('What year were you born? ').strip()
try:
    birth_year_actual = int(birth_year)
    age = 2024 - birth_year_actual
    print(f'Your age is: {age}')
except ValueError:
    print("Please enter a valid year as a number.")
