n=int(input('\n\tEnter the number till fibonacci must be found  : '))

n1=0
n2=1
res=0

for i in range(0,n+1):
    n1=n2
    n2=res
    res=n1+n2
    print(res)