# 8-11. Archived Messages:
messages = [
    'Can’t believe these con men are not yet being PROSECUTED. Pathetic!',
    'Proud of you Natalie!',
    '...And I had to put up with these losers and still run a Country, AND VERY WELL!'
]

sent_messages = []

def send_messages(messages, sent_messages):
    """
    Print each text message.
    Move each message to a new list
    """
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print(f"\nMessages: {messages}")
print(f"Sent messages: {sent_messages}")