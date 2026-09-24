def Even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
x=int(input("enter num1:"))
y=int(input("enter num2:"))
Even(x,y)