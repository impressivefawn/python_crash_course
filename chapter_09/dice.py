# 9-13. Dice:
from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d6 = Die(10)

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print(results)


# Make a 20-sided die, and show the results of 10 rolls.
d6 = Die(20)

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print(results)