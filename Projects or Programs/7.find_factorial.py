n=int(input("Enter the num to find factorial : "))

def factorial(n):
    if n==0:
        return 1
    else:
        return (n*factorial(n-1))

print('Answer : ',factorial(n))