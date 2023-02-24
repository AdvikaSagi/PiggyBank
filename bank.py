#AccountNumber,FirstName,LastName,Balance Ex.1,Rahul,Marian,199999

def createAccount():
    readfile = open('accountNumber.txt', 'r')
    accountNumber = readfile.read()
    aNumber = int(accountNumber) + 1
    accountNum = str(aNumber)
    readfile.close()
    fileHandling = open('accountNumber.txt', 'w')
    fileHandling.write(accountNum)
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
        5. Exit""")
        option = input("Enter your option: ")

        if option == '5':
            showScreen = False

        