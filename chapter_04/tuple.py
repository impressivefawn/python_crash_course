# 4-13. Buffet:
menu = ('Salmon sandwich', 'Egg white omelette', 'Fruit plate', 'Oatmeal porridge', 'Orange juice')
print('Original menu:')
for dish in menu:
    print(f'    {dish}')

# TypeError: 'tuple' object does not support item assignment
# menu[-1] = 'Apple juice'

menu = ('Salmon sandwich', 'Egg white omelette', 'Fruit plate', 'Rice porridge', 'Carrot juice')
print('\nRevisited menu:')
for dish in menu:
    print(f'    {dish}')