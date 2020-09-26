# 5-8. Hello Admin:
usernames = ['tatOCkso', 'FLOUPTit', 'CeRypowN', 'admin', 'eonalbEw']

for username in usernames:
    if username.lower() == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
print('')

# 5-9. No Users:
usernames = []
if usernames:
    for username in usernames:
        if username.lower() == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10. Checking Usernames:
current_users = ['xogreSBu', 'faLvERBo', 'meNsoLIn', 'hIraTEPh', 'yPtISIma']
new_users = ['yPtISIma', 'rNITHoNE', 'LUBtaBio', 'MeNsoLIn', 'ENdAYenS']

current_users_lower = [current_user.lower() for current_user in current_users]
print(f"\n{current_users_lower}")

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} has already been used. Please enter a new username.")
    else:
        print(f"{new_user} is available.")

# 5-11. Ordinal Numbers:
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("\nOrdinal number list:")
        print(number, "1st")
    elif number == 2:
        print(number, "2nd")
    elif number == 3:
        print(number, "3rd")
    else:
        print(number, f"{number}th")