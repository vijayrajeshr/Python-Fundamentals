n = [1, 2, 3, 4, 5]

print(n)
n.extend([56, 2, 12])
print(n)

n.append(5)
print(n)
print(n.count(5))

print(n.index(56))
print(n.index(5,5))
print(n.index(5))

n.insert(1, 45)
print(n)

my_num = n.pop(2)
print(my_num)
print(n)

n.remove(12)
n.remove(5)
print(n)

n.sort()
print(n)
n.reverse()
print(n)
