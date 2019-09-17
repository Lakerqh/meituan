def f(x):
    return x + 1
r = map(f, [1,2,3])
print(list(r))

def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd,[1,2,3,4,5,6,7]))
print(l)

print(sorted([23,0,-23,4,5]))