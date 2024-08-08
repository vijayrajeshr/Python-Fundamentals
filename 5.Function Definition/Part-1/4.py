def SumList(lst):
	s=0
	for n in lst:
		s+=n
	return s

print("Sum of List :",SumList([1,2,3,4,5]))
print("Sum of 15 Number using Range : ",SumList(list(range(1,10))))