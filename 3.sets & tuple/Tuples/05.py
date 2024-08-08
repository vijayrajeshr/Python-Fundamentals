# Changing tuple values (Only on nested list)
my_t = (4, 2, 3, [6, 5])
# my_t[1] = 9   # Not Possible
my_t[3][0] = 9      
print(my_t)

my_t = ('a', 'p', 'p', 'l', 'e')  # Reassigning to Tuple
print(my_t)

print(my_t.count('p'))   #Tuple Methods (2 Methods)
print(my_t.index('l'))

del my_t    # Deleting Tuple
print(my_t)
