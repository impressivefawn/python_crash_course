# 8-10. Sending Messages:
messages = [
    'THE FAKE NEWS MEDIA IS THE REAL OPPOSITION PARTY!',
    'Why does Joe Biden plagiarize foreign politicians so much?',
    'VOTE TRUMP CALIFORNIA!'
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

send_messages(messages, sent_messages)

print(f"\nMessages: {messages}")
print(f"Sent messages: {sent_messages}")