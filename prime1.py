n=int(input("enter a number"))
if n==1 or n==0 :
    print("enter valid prime number")
c=0    
for i in range(2,n+1):
    if n%i==0:
        c=c+1
if c>2:
    print("not prime")
else:
        print("prime")
