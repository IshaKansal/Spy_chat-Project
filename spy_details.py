from datetime import datetime
class Spy:
    def __init__(self, name, age, rating, is_online):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = is_online
        self.chats = []
        self.current_status_message = None
        self.average = 0
        self.message_no = 0
        self.no_of_words = 0

class Chat_Message:
    def __init__(self, message, sent_by_me, choice, no_of_words):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
        # If messages are from spy's friend then calculating average no of words spoken by that spy friend
        if not sent_by_me:
            # Incrementing the message no by 1
            friends[choice].message_no += 1
            # Incrementing no of words
            friends[choice].no_of_words += no_of_words
            # Calculating average
            friends[choice].average = friends[choice].no_of_words/friends[choice].message_no

# Initializing spy with default details
spy = Spy('Mr Bond', 24, 4.2, True)

# Adding some default friends
friend_one = Spy('Mr abc', 22, 4.25, True)
friend_two = Spy('Ms xyz', 21, 4.3, False)
friend_three = Spy('Dr pqr', 25, 4.5, True)

# List of friends
friends = [friend_one, friend_two, friend_three]
