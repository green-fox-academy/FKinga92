accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def balance_of_cash(number):
    if any(d['account_number'] == int(number) for d in accounts):
        for i in range(len(accounts)):
            if accounts[i]['account_number'] == int(number):
                return accounts[i]['client_name'] + ": " + str(accounts[i]['balance'])
    else:
        print("404 - account not found")


def transfer(num1, num2, amount):
    if amount > 0:
        if any(d['account_number'] == int(num1) or d['account_number'] == int(num2) for d in accounts):
            for i in range(len(accounts)):
                if accounts[i]['account_number'] == int(num1):
                    accounts[i]['balance'] -= float(amount)
            for i in range(len(accounts)):
                if accounts[i]['account_number'] == int(num2):
                    accounts[i]['balance'] += float(amount)
        else:
            print("404 - account not found")
    else:
        print("You cannot transfer an amount smaller than 0.")
        
