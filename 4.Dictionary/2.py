# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares) #True
print(2 not in squares) #True
print(49 in squares) # False
for i in squares:
    print(squares[i])
