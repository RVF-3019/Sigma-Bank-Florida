import csv








class CheckingAccount:
    def __init__(self, account_number):
        self.account_number = account_number
    balance = 10000
    def return_balance(self, balance):
         print(balance)
    def Here(self):
        print("Checking Account balance:")


class SavingAccount:
    def __init__(self, account_number):
        self.account_number = account_number
    def Here(self):
        print("Savings Account balance:")
    balance = 10000
    def return_balance(self, balance):
        print(balance)


with open('Accounts.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count ==0:
            {",".join(row)}
            #line_count+=1
            g = int((row["id"]))
            if ((g % 10) == 1):
                CheckingAccount.Here(g)
                CheckingAccount.return_balance(g,float((row["account balance"])))

            else:
                SavingAccount.Here(g)
                SavingAccount.return_balance(g,float((row["account balance"])))

            #line_count+=1



