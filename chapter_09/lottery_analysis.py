# 9-15. Lottery Analysis:
from random import choice

def get_winning_ticket(possibilities):
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    for item in played_ticket:
        if item not in winning_ticket:
            return False
    return True

def make_random_ticket(possibilities):
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

max_tries = 1000000

while not won:
    my_ticket = make_random_ticket(possibilities)
    plays += 1
    won = check_ticket(my_ticket, winning_ticket)
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
