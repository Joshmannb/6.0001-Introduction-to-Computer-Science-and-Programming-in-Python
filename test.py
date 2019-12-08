a = 'a_ _ le'
b = list(''.join(a.split()))
print(a)
for i in a:
    print(i)
    if i == '_':
        b.remove(i)
print(b)