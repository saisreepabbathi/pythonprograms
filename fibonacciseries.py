n=int(input("enter the fibonacci len:"))
a,b=0,1
print("{}\n{}".format(a,b))
temp=0
for i in range(2,n):
    temp=a+b
    a=b
    b=temp
    print(temp)

