x = '' 
print(x.isspace())
#returns False because there is no space in the string.
y = ' '
print(y.isspace())
#returns True because the only thing existing in that string is a space.
z = 'a  '
print(z.isspace())
#returns False beacause the space exists but other characters also exist.