a = {'a': 1}
a['b'] = 2
for i in a.items():
    print(i)
c = list(a.items())
print(c)