
setData = { 2,3,1,4,5 }
setData.add(22)

setData.discard(1)
print(type(setData))
print(setData)

for v in setData:
    print(v)

frozenData = frozenset(setData)
print(type(frozenData))
#frozenData.add(56) # błąd!

for value in frozenData:
    print(value)

