filename = 'chapter_10/programming_poll.txt'

print("Enter 'quit' when you are finished.")
while True:
    response = input("\nWhy do you like programming? ")
    if response == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{response}\n")