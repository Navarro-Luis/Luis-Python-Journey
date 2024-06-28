from translate import Translator

translator = Translator(to_lang = 'ja')

try: 
    with open('./excercise.txt',mode ='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
except FileNotFoundError as err:
    print('Check you file path silly!')

    # this module is outdated so this isnt going to work, maybe re
    #visit with safe.