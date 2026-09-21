username=input("enter the username:")
password=input("enter the password:")
if username=="admin" and password=="admin123":
    print("login successful")
elif username=="admin" and password!="admin123":
    print("invalid password")
elif username!="admin" and password=="admin123":
    print("invalid username")
else:
    print("invalid username and password")