#sample problem . conditional statements
#check eligiblity for scholarship which the score >=8.50

score=float(input("\n\tEnter Score  : "))

if score<0 and score>10:
    print("\n\tEnter valid score. Try again!")

elif score>8.50:
    print("\n\tYou are eligible for scholarship")

else:
    print("\n\tSorry you are not eligible.")