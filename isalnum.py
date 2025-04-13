x = 'birthday'
print(x.isalnum())
#returns true because all items are alphabets

y = '21st birthday'
print(y.isalnum())

#returns False because space is included

z = '21stbirthday'
print(z.isalnum())

#returns true because all existing items are alphanumeric