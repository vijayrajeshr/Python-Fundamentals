import random
print("Random 0 to 1 : ",random.random())
print("Random Range 0 to 5 : ",random.randrange(5))
print("Random Range 50 to 100 : ",random.randrange(50,100))
print("Random Range 101 to 999 Odd : ",random.randrange(101,1000,2))

print("Random Integer 10,50 : ",random.randint(10,50))
print("Random Float 10,50 : ",random.uniform(10,50))

course=["HDCA","HDCP","DCA","DCP","ADCP"]
print("Random Value from Course : ",random.choice(course))
random.shuffle(course)
print("Shuffle Value from Course : ",course)
