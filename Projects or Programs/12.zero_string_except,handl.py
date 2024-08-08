n1 = int(input("\n\tEnter the numerator : "))
n2 = int(input("\n\tEnter the denominator : "))

try:
    ans = n1 / n2
    print("\n\tANS : ", ans)
except ZeroDivisionError:
    print("\n\t0 Division error")
except ValueError:
    print("\n\tInvalid input. Please enter integers only.")
finally:
    print("\n\t--- End of Compilation ---")
