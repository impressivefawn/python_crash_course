# 4-10. Slices:
odds = []
for i in range(1, 21, 2):
    odds.append(i)

print(f'The first three items in the list are: {odds[:3]}')
print(f'Three items from the middle of the list are: {odds[5:8]}')
print(f'The last three items in the list are: {odds[-3:]}')


# 4-11. My Pizzas, Your Pizzas:
pizzas = ['Quattro formaggi', 'Hawaiian', 'Margherita', 'Capricciosa']
friend_pizzas = pizzas[:]
pizzas.append('BBQ Chicken')
friend_pizzas.append('Pepperoni')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
  
print('\nMy friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)

# 4-12. More Loops:
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friends_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
print('My favorite foods are:')
for food in my_foods:
    print(food)

print('\nMy friend\'s favorite foods are:')
for food in friends_foods:
    print(food)