# set mode to 'r' to read
# set mode to 'W' to write
# set mode to 'r+' to read/write
# set mode to 'a' to append at end of file
try:
    with open('wow.txt', mode = 'r') as my_file:
        text = my_file.read()
    print(text)

except FileNotFoundError as err:
    print('file does not exist')
    raise err



