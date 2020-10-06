# 7-9. No Pastrami:
sandwich_orders = ['Pastrami', 'Beirute', 'Mortadella', 'Pastrami', 'Runza', 'Tavern', 'Vegemite', 'Pastrami']
finished_sandwiches =[]
print("\nThe deli has run out of pastrami.")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    if current_order == 'Pastrami':
        continue
    else:
        print(f"We are preparing {current_order} sandwich.")
        finished_sandwiches.append(current_order)

print(finished_sandwiches)