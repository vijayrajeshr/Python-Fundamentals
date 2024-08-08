#Nested if statement

na=input("Please Enter your Name :")
ci=input("Are you an Indian[Y/N]")

if((ci=="Y") or (ci=="y")):
	age=int(input("Please Enter your Age"))
	if(age>18):
		print("\n",na,"is Eligible for Voting")
	else:
		print("\n",na," is Not Eligible for Voting")
elif((ci=="N") or (ci=="n")):
	print("\n Sorry ", na ," Indians only Eligible for Voting")
else:
	print("\n Invalid Selection")
