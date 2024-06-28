#walrus
a = 'hellooooooooooo'

if (len(a) >10):
    print(f'too long {len(a)} elements')

## no bueno because you are repeating urself. calcing len(a) twice. better:

if ((n := len(a))> 10):
    print(f'too long {n} elements')

#accessing global variables