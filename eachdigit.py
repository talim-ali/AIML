def print_digit(n):
    while n>0:
        digit=n%10
        n=n//10
        print(digit)
x=int(input("enter a number:"))
print_digit(x)