# 3-4. Guest List:
guest_list = ['Neil deGrasse Tyson', 'Richard Dawkins', 'Alan Turing']
print(f'{guest_list[0]}, you can come for a dinner')
print(f'{guest_list[1]}, you can come for a dinner')
print(f'{guest_list[2]}, you can come for a dinner')

# 3-5. Changing Guest List:
print(f'Sorry but {guest_list[2]} can\'t come')
# Replacing a guest
guest_list[-1] = 'Adam Smith'
print(f'{guest_list[0]}, you can come for a dinner')
print(f'{guest_list[1]}, you can come for a dinner')
print(f'{guest_list[2]}, you can come for a dinner')

# 3-6. More Guests:
# Sending an invintation
print(f'{guest_list[0]}, you can take one of your friends')
print(f'{guest_list[1]}, you can take one of your friends')
print(f'{guest_list[2]}, you can take one of your friends')

# Adding more guests to the list
guest_list.insert(0, 'Carl Sagan')
guest_list.insert(2, 'Christopher Hitchens')
guest_list.append('David Ricardo')

# Sending an invintation
print(f'{guest_list[0]}, you can come for a dinner')
print(f'{guest_list[1]}, you can come for a dinner')
print(f'{guest_list[2]}, you can come for a dinner')
print(f'{guest_list[3]}, you can come for a dinner')
print(f'{guest_list[4]}, you can come for a dinner')
print(f'{guest_list[5]}, you can come for a dinner')

# 3-7. Shrinking Guest List:
print('Unfortunately, we can invite only two of you')

print(f'{guest_list.pop()}, we are really sorry. We can\'t invite you this time')
print(f'{guest_list.pop()}, we are really sorry. We can\'t invite you this time')
print(f'{guest_list.pop()}, we are really sorry. We can\'t invite you this time')
print(f'{guest_list.pop()}, we are really sorry. We can\'t invite you this time')

print(f'{guest_list[0]}, you are still invited. Please come for a dinner')
print(f'{guest_list[1]}, you are still invited. Please come for a dinner')

del guest_list[0]
del guest_list[0]

print(guest_list)