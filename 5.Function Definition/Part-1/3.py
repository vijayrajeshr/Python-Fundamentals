def sum(*num):
	s=0
	for n in num:
		s+=n
	return s

print("Sum of 2 and 7 :",sum(2,7))
j=sum(78,89,45,75)
print("Sum of :",j)
