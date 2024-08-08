print('\n\t--- ZeroDivisoon Check ---')

n1=float(input('\n\tEnter the numerator : '))
n2=float(input('\n\tEnter the denominator : '))

try:
    ans=n1/n2
    print('\n\tThe answer is : ',ans)

except ZeroDivisionError:
    print('\n\tError! The Denominator cannot be zero.')

finally:
    print('\n\t-------- End of Program --------')