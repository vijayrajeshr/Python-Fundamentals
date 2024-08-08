n1 = int(input('\n\tEnter numerator : '))
n2 = int(input('\n\tEnter denominator : '))

try:
    ans = n1 / n2
    print(ans)
except ZeroDivisionError:
    print("\n\tDivision by zero is not defined")
finally:
    print("\n\t---Program is compiled---")
    