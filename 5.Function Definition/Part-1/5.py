def FunLIst(lst):
	print("Passed List :",lst)
	lst.extend([5,6,7,8,9])
	print("Updated in Function : ",lst)

lst=[1,2,3,4]
FunLIst(lst)
print("After Call:",lst)