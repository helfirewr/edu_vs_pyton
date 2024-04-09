text='Hello'
print(dir(text))
print(text.upper())
x=256
y=256
print(x is y)
x, y = 256,256
print(x is y)
listOne=['one', 'two']
listTwo=listOne
print(listOne is listTwo)
listOne.append('3')
print(listOne)
print(listOne is listTwo)
listThree=['one', 'two', '3']
print(listOne is listThree)