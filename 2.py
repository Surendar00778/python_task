# Read the number of accounts
numOfAccounts = int(input())

# Read the list of account balances as space-separated integers and split them into a list
balances = list(map(int, input().split()))

# Initialize a variable to count the number of negative balances
negative_count = 0

# Iterate through the list of balances
for balance in balances:
    if balance < 0:
        negative_count += 1

# Print the number of dormant accounts with a negative balance
print(negative_count)
