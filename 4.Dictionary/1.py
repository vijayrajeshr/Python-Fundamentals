# Dictionary Methods
std={"Sno":1,"SName":"Jey"}
marks={"Total":500,"Result":"Pass","Rank":1}
std.update(marks)
print("Std Info:",std)

grade=marks.copy();
marks.clear()
print("Grade Info: ",grade)
