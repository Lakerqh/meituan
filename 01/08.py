from collections import Iterable

list = [1,2,3,4,5]
print(list[0:3])

s = {'a':1,'b':2}
for key in s.values():
    print(key)

str = 'ABC'
for key in str:
    print(key)

print(isinstance('abc',Iterable))


