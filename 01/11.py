import functools

int2 = functools.partial(int,base=2)
print(int2('00000001'))

print(int('123'))
print(int('123',base=8))
print(int('123',base=16))

