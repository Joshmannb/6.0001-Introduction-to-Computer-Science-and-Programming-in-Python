a = {'a':1, 'b':2, 'c':3}
b = a.copy()
print(a is b)
del(a['a'])
print(a)