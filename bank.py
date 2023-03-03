#AccountNumber,FirstName,LastName,Balance Ex.1,Rahul,Marian,199999


def addMoney():
    name = input('Enter the name of the person whose account yur adding money to: ')
    money = int(input('Enter the amount your adding: '))
    fileHandler = open('account.txt','r')
    files = fileHandler.readlines()
    for line in files:
        if name in line:
          details= line.split(",")
    
    d = int(details[-1]) + money
    


def seeAccount():
    name = input("Enter the first name of the person's balance you want to see: ")
    fileHandler = open('account.txt','r')
    files = fileHandler.readlines()
    for line in files:
        if name in line:
          details= line.split(",")
          #print(details)
          print(f"The balance for {name} is : ",details[-1])


def createAccount():
    first_name = input('Enter your first name: ')
    surename = input('Enter you surename: ')
    number = input('Enter a phone number: ')
    balance = input('Enter the the amount of money in ypur accaount: ')
    readfile = open('accountNumber.txt', 'r')
    accountNumber = readfile.read()
    aNumber = int(accountNumber) + 1
    accountNum = str(aNumber)
    readfile.close()
    writeAccount = open('accountNumber.txt', 'w')
    writeAccount.write(accountNum)
    account = accountNum+','+ first_name+','+ surename+','+ number+','+ balance
    fileHandling = open('account.txt', 'w')
    fileHandling.write(account)
    fileHandling.close()


def display():
    showScreen = True
    while showScreen == True:
        print("""Welcome to PiggyBank!
        
        Please select one of the options below:
        1. Create an account
        2. Add Money to account
        3. Withdraw Money from account
        4. Check balance in account
        5. Delete account(don't choose yet)
        5. Exit""")
        option = input("Enter your option: ")

        if option == '6':
            showScreen = False

        if option == '4':
            seeAccount()
            showScreen = False

        if option == '1':
            createAccount()
            showScreen = False

        if option != '6':
            trueStatus = input("Whould you like to continue? y/n: ")#asking if you want to coninue
            if trueStatus == 'y':
                showScreen = True

            elif trueStatus == 'n':
                showScreen =  False

            else:
                print("Sorry, I didn't understand.")
                trueStatus = input("Whould you like to continue? y/n: ")

                if trueStatus == 'y':
                    showScreen = True

                elif trueStatus == 'n':
                    showScreen =  False
                    print("Thank you for using PiggyBank. Bye")
                else:
                    print("Thank you for using PiggyBank. Bye")

display()

        