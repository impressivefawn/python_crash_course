number = input("Guess a whole number: ")
number = int(number)

if number % 10 != 0:
    print(f"\nThe number {number} is not a multiple of 10. Better luck next time!")
else:
    print(f"\nThe number {number} is a multiple of 10.")