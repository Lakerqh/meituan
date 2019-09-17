from io import StringIO
f = StringIO()
f.write('hello')

s = f.readline()
print(s)


