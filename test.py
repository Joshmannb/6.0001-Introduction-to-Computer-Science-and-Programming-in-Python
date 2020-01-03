a = 'Office Microsoft do you?  '
b = 'Microsoft Office'
c = [x.strip(',./`~!?;@#$%^&*()_+') for x in a.split()]
d = ' '.join(c)
print(b in a)