# 5-3. Alien Colors #1:
alien_color = 'yellow'
if alien_color == 'green':
    points = 5
else:
    points = 0

print(f"\nYou earned {points} points for shooting down a {alien_color} alien.")

# 5-4. Alien Colors #2:
alien_color = 'red'
if alien_color == 'green':
    points = 5
else:
    points = 10

print(f"\nYou earned {points} points for shooting down a {alien_color} alien.")

# 5-5. Alien Colors #3:

alien_color = 'green'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print(f"\nYou earned {points} points for shooting down a {alien_color} alien.\n")

# 5-6. Stages of Life:
age = 8
if age < 2:
    print('The person is a baby.')
elif age < 4:
    print('The person is a toddler.')
elif age < 13:
    print('The person is a kid.')
elif age < 20:
    print('The person is a teenager.')
elif age < 65:
    print('The person is an adult.')
elif age >= 65:
    print('The person is an elder.')
print('')

# 5-7. Favorite Fruit:
fruits = ['Apricot', 'Grapes', 'Orange']

if 'Apricot' in fruits:
    print("You really like apricots!")
if 'Grapes' in fruits:
    print("You really like grapes!")
if 'Orange' in fruits:
    print("You really like oranges!")
if 'Mango' in fruits:
    print("You really like mangoes!")
if 'Tangerine' in fruits:
    print("You really like tangerines!")