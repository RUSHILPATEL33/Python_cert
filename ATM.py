balance = 10000
pin = 123456
a=input("Enter your account number:")
Enter_amount=int(input("Enter Amount:"))
Enter_pin=int(input("Enter your pin"))
Remained_balance= balance-Enter_amount
if Enter_pin !=pin:
    print("Incorrect pin")
elif Enter_amount<0:
    print("invalid ammount")
    
elif Enter_amount>balance:
    print("Insufficient balance")
else:
    print("Amount withdrawed")
    print("Amount remained after withdrawing money",Remained_balance)
        
     
        
    