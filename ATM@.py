print("--Welcome to ATM--")
pin=123
balance=10000
guess = int(input("Enter pin"))

if guess == pin:
    print("What you want to do")
    print("Withdraw Money (Enter 1)")
    print("Check balance (Enter2)")
    
    task = int(input("Enter choice (1 or 2): "))
    
    if task == 1:
        askMoney = int(input("Enter amount to withdraw:"))
        
        if askMoney <= balance:
            print("Withdraw successfully")
            balance -= askMoney
            print(balance)
        else:
            print("Balance Insuuficent")
        
        if task ==2:
            print(balance)
    else:
        print("incorrect pin.")