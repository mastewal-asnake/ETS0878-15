x = '11'
print(x.isdigit())

#True

y = '1 1'
print(y.isdigit())

#False because of the space

z = 'word11'
print(z.isdigit())

#False because of 'word'

a = '11/'
print(a.isdigit())

#False because of /