print("welcome to the calculator")

def add(n1,n2):
    return n1+n2

def mul(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2

continues=True

while continues:
    users_input=input("enter the operation you like to perform")
    if users_input=="Exit":
        break

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

if users_input=="add":
    print(add(num1,num2))

elif users_input=="mul":
    print(mul(num1,num2))

elif users_input=="sub":
    print(sub(num1,num2))

elif users_input=="div":
    print(div(num1,num2))

else:
    print("Exit")



