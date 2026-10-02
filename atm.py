print("welcome to the atm")

balance=10000
pin="123"

print("insert atm")
user_pin=input("enter your pin")
if user_pin==pin:
    print("press for 1 balance check")
    print("press for 2 cash withdraw")
    print("press for 3 deposit")
    print("press for 4 exit")

    user_press=input("enter your press")
    if user_press=="1":
        print(f"your balance is {balance}")

    elif user_press=="2":
        withdraw_amount=int(input("enter your with draw amount"))
        if withdraw_amount<=balance:
            balance=balance-withdraw_amount
            print("your withdraw is succesful")
            print(f"your remaining amount is{balance}")




        else:
            print("insuddicient balance") 

    elif user_press=="3":
            deposit_amount=int(input("enter your deposit amount"))
            balance=balance+deposit_amount
            print(f"your deposit amount is{deposit_amount} and new balance is {balance}")


    elif user_press=="4":
        print("exit")

else:
        print("invalid option")

        
    