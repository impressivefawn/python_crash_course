# 7-8. Deli:

sandwich_orders = ['Beirute', 'Mortadella', 'Runza', 'Tavern', 'Vegemite']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"We are preparing {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("")
for sandwich in finished_sandwiches:
    print(f"You {sandwich} is ready!")