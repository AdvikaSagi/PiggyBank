#AccountNumber,FirstName,LastName,Balance Ex.1,Rahul,Marian,199999


def addMoney():
    num = input('Enter your account number: ')
    money = int(input('Enter the amount your adding: '))
    fileHandler = open('account.txt','r')
    files = fileHandler.readlines()
    for line in files:
        details= line.split(",")
        if num == details[0]:
            f = open('bank_balance/' + details[0] + '.txt', 'r')
            d = f.readline()
            a = int(d) 
            a += money
            amount = str(a)
            balance_file = open('bank_balance/' + details[0] + '.txt', 'w')
            balance_file.write(amount)
            balance_file.close()
            read = open('bank_balance/' + details[0] + '.txt', 'r')
            print('Your new balance is ', read.read())


def withdrawMoney():
    num = input('Enter your account number: ')
    money = int(input('Enter the amount your withdrawing: '))
    fileHandler = open('account.txt','r')
    files = fileHandler.readlines()
    for line in files:
        details= line.split(",")
        if num == details[0]:
            f = open('bank_balance/' + details[0] + '.txt', 'r')
            d = f.readline()
            a = int(d) 
            a -= money
            amount = str(a)
            balance_file = open('bank_balance/' + details[0] + '.txt', 'w')
            balance_file.write(amount)
            balance_file.close()
            read = open('bank_balance/' + details[0] + '.txt', 'r')
            print('Your new balance is ', read.read())
          
    
    
    


def seeAccount():
    num = input("Enter your account number: ")
    fileHandler = open('account.txt','r')
    files = fileHandler.readlines()
    for line in files:
        details= line.split(",")
        if num == details[0]:
          file = open('bank_balance/' + details[0] + '.txt', 'r')
          read = file.read()
          
          #print(details)
          print(f"The balance for account number {num} is : ", read)


def createAccount():
    first_name = input('Enter your first name: ')
    surename = input('Enter you surename: ')
    number = input('Enter a phone number: ')
    balance = input('Enter the the amount of money in your account: ')
    readfile = open('accountNumber.txt', 'r')
    accountNumber = readfile.read()
    aNumber = int(accountNumber) + 1
    accountNum = str(aNumber)
    readfile.close()
    writeAccount = open('accountNumber.txt', 'w')
    writeAccount.write(accountNum)
    account = accountNum+','+ first_name+','+ surename+','+ number+','+ accountNum + '.txt' + '\n'
    fileHandling = open('account.txt', 'a')
    fileHandling.write(account)
    fileHandling.close()
    print('Your account number is ', accountNum)
    f = open('bank_balance/' + accountNum + '.txt', 'w')
    f.write(balance)
    f.close()


def display():
    showScreen = True
    while showScreen == True:
        print("""Welcome to PiggyBank!
        
        Please select one of the options below:
        1. Create an account
        2. Add Money to account
        3. Withdraw Money from account
        4. Check balance in account
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
        if option == '2':
            addMoney()
            showScreen = False
        if option == '3':
            withdrawMoney()
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

        