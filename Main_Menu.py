

class locker():
    def __init__(self, x ,y):
        self.x = x
        self.y=y







name = "James Smith"
Age = 30
salary = 60000
credit_score = 800
credit_card_balance = 400
checking_balance = 3000
saving_balance = 15000
minimum_payment = 20
Address_Variable = "Tropico Ambassy, 34 Cory Street, Miami"


Continue = True
Continue2 = True


def Logout_A():
    if Continue:
        Stream = input("Do you wanna leave?   ")
        if Stream.upper() == 'Y':
            Continue2 = False
        else:
            Continue2 = True

def Choose_Account():
    Checking = False
    Stream = input("Do you want to use your Savings or Checking account? ")
    if Stream.upper() == 'S':
        Checking = False
    else:
        Checking = True
    return Checking




# CCB, CB, SB, MP,AGE,SAL, Address

def key_listener_A(CCB: int, CB: int, SB: int, MP: int, AGE: int, SAL: int, ADDRESS: str):
    global name
    global Age
    global salary
    global credit_score
    global checking_balance
    global credit_card_balance
    global saving_balance
    global minimum_payment
    global Address_Variable

    Address = ADDRESS
    Action = input(" ENTER KEY FOR ACTION:")

    if Action.upper() == "I":
        print(f'CREDIT CARD BALANCE: {credit_card_balance}')
        print(f'CHECKING BALANCE: {checking_balance}')
        print(f'SAVING BALANCE:  {saving_balance}')
        print(f'MINIMUM PAYMENT:  {minimum_payment}')
        print(f'{name}')
        age = AGE
        sal = SAL
        print(f'ADDRESS: {Address}')
        change_Adress = False
        return True

    if Action.upper() == "A":
        change_name = input("Do you want to change your Adress?")
        if change_name.upper() == "Y":
            change_Adress = True
            print(Address)
        if change_name.upper() != "Y":
            change_Adress = False
            print(Address)
            return Logout_A()

        if change_Adress == True:
            new_Adress = input("What is your new address?")
            print(new_Adress)
            return Logout_A()

        change_Adress = False


    elif Action.upper() == "C":
        print(f"${CCB}")
        if Choose_Account():
            current_account = checking_balance
            CB = current_account
        else:
            current_account = saving_balance
            CB = current_account

        Action = input('''Do you want to send a total(T), minimum(M), regular_payment(R/P) payment?


ENTER :         T                          M                          R/P            RETURN



    ''')

        if Action.upper() == "T":
            if CB >= CCB:
                CB = CB - CCB
                CCB = CCB - CCB
                current_account = CB
                credit_card_balance = CCB
                print(f'Checking Balance: {CB}   Credit Card Balance: {CCB}')


        elif Action.upper() == 'M':
            if CB >= CCB:
                CB = CB - MP
                CCB = CCB - MP
                current_account = CB
                credit_card_balance = CCB
                print(f'Checking Balance: {CB}   Credit Card Balance: {CCB}')



        elif Action.upper() == 'R' or Action.upper() == 'P':
            if CB >= CCB:
                payment = int(input("ENTER PAYMENT: $ "))
                CB = CB - payment
                CCB = CCB - payment
                current_account = CB
                credit_card_balance = CCB
                print(f'Checking Balance: {CB}   Credit Card Balance: {CCB}')

        if Choose_Account:
            checking_balance = CB
        else:
            saving_balance = CB
        return Logout_A()


    elif Action.upper() == "A":
        print(f"CHECKING BALANCE:     ${CB}")
        print('''

            ADDING MONEY         TRANSFER OF FUNDS          CHECKING ENTRIES          RETURN


            ''')

        checking_action = input(" Please enter A/M, T/O/F, C/E, or R")

        if checking_action.upper() == "A" or checking_action.upper() == "M":
            print(f'${CB}')

    else:
        print(f'CREDIT CARD BALANCE: ${CCB}')
        print(f'CHECKING BALANCE: ${CB}')
        return Logout_A()

    return True


def main_menu():
    print('''
                    MENU OF ACCOUNT

    CREDIT CARD       INFO           ACCOUNT     CREDIT SCORE        LOG OUT


''')


# key_listener_A(credit_card_balance, checking_balance, saving_balance, minimum_payment, Age, salary,
#                 Address_Variable)


while Continue:




    main_menu()
    Continue2 = key_listener_A(credit_card_balance, checking_balance, saving_balance, minimum_payment, Age, salary,
                               Address_Variable)
    print(Continue2)


    if (Continue != Continue2):
        print('''


                                    YOU ARE LEAVING THE ATM

                                        HAVE A NICE DAY!


        ''')
        break