print('Hello, Django girls!')
print(True and 1==1)

name = 'Zsófi'

if 3 > 2:
    print('It works!')
else:
    print('it does not work')
#Please don't change the name
name = 'Sonja'

def hi():
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi()

def hello():
    print('Hello there!')
    print('How are you?')

hello()

def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

girls = ['Sonja', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)
