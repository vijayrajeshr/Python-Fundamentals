
import datetime

print ("Current Date and Time is 	: " , datetime.datetime.now())
print ("Current Date and Time is 	: " ,datetime.datetime.now().strftime("%y-%m-%d %H:%M"))
print ("Current Date and Time is 	: " ,datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

print ("Current Year(2 Digit)		: ", datetime.date.today().strftime("%y"))
print ("Current Year(4 Digit)		: ", datetime.date.today().strftime("%Y"))
print ("Current Month(3 Digit)		: ", datetime.date.today().strftime("%b"))
print ("Current Month(Full Name)	: ", datetime.date.today().strftime("%B"))
print ("Week of the Year		: ", datetime.date.today().strftime("%W"))
print ("Weekday of the Week 		: ", datetime.date.today().strftime("%w"))
print ("Day of year			: ", datetime.date.today().strftime("%j"))
print ("Day of the month 		: ", datetime.date.today().strftime("%d"))
print ("Day of Week(3 Digit)		: ", datetime.date.today().strftime("%a"))
print ("Day of Week(Full Name)		: ", datetime.date.today().strftime("%A"))


dd=datetime.datetime(1947,8,15,8, 44, 4)
print ("\nCurrent Date and Time is 	: " , dd)
print ("Current Date and Time is 	: " ,dd.strftime("%y-%m-%d %H:%M"))
print ("Current Date and Time is 	: " ,dd.strftime("%Y-%m-%d %H:%M"))

print ("Current Year(2 Digit)		: ", dd.strftime("%y"))
print ("Current Year(4 Digit)		: ", dd.strftime("%Y"))
print ("Current Month(3 Digit)		: ", dd.strftime("%b"))
print ("Current Month(Full Name)	: ", dd.strftime("%B"))
print ("Week of the Year		: ", dd.strftime("%W"))
print ("Weekday of the Week 		: ", dd.strftime("%w"))
print ("Day of year			: ", dd.strftime("%j"))
print ("Day of the month 		: ", dd.strftime("%d"))
print ("Day of Week(3 Digit)		: ", dd.strftime("%a"))
print ("Day of Week(Full Name)		: ", dd.strftime("%A"))


