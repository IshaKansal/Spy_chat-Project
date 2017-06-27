# Importing libraries
from spy_details import spy, Spy, friends, Chat_Message
from steganography.steganography import Steganography
from termcolor import colored

# starting chat
print "Hello! Let's get Started"

# defining a list with some default status in it
status_message = ["My name is Bond,James Bond", "Shaken,not stirred.."]

# Function for categories of spy
def rating_criteria(spy_rating):
    # categorizing  spy on the basis of rating
    if spy_rating > 4.5:
        print colored("u r genious", 'blue')
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print colored("u r good one", 'blue')
    elif spy_rating > 2.5 and spy_rating <= 3.5:
        print colored("u can do better", 'blue')
    else:
        print colored("u can help others", 'blue')

# Function for validating age
def valid_age(spy_age):
    # checking the eligibility of spy
    if spy_age > 12 and spy_age <= 50:
        return True
    else:
        return False

# Function for validating name
def valid_name(spy_name):
    # removing the space before and after in input
    spy_name = spy_name.strip()
    # splitting input with space   # split is used so that we can input like "Isha Kansal" here we need space
    spy_name1 = spy_name.split()
    # variables declaration
    # "v" for characters
    v = 0
    # iv for digits,space and special symbols
    iv = 0
    # checking the input from user after splitting it
    for s in spy_name1:
        if s.isalpha():
            # if only character...increment "v"
            v += 1
        else:
            # other than character..increment "iv"
            iv += 1
    # checking if 'iv' is 0 or not because if iv is incremented at least one time the input is invalid
    if iv > 0:
        # if not zero..return false
        return False
    elif iv == 0:
        # if zero..return true
        return True

# declaring i to maintain the index while printing friends
i = 0
# Function for print friends on the basis of their status given in 'arg'
def print_friend(arg):
    global i
    for friend in friends:
        if friend.is_online == arg:
            i = i+1
            print "%d. %s  %d  %.2f" % (i, friend.name, friend.age, friend.rating)

# Function for selecting a Friend
def select_friend():
    # printing online friends
    print colored("Online Friends", 'blue')
    print_friend(True)
    # printing offline friends
    print colored("Offline Friends", 'blue')
    print_friend(False)
    # reinitialise i so that index of friends while printing will start from 1 when this function is called again
    global i
    i = 0
    # saying the spy to select the index of friend and storing it
    friend_choice = int(raw_input("Select Friend"))
    # Checking if spy has chosen from above list or entered invalid index.....
    if len(friends) >= friend_choice:
        # returning the index  selected by  spy " -1 because in list index start from 0'
        return friend_choice-1
    # If not chosen from above list....warn the spy and again chose from spy
    else:
        print colored("You enter a wrong index of your  friend!!!! Please, select again!!!!", 'red')
        return select_friend()

# Function to send a message
def send_message():
    # saying the spy to select friend to whom want to send secret message
    friend_choice = select_friend()
    print colored("Send a message to your friend %s" % friends[friend_choice].name, 'blue')
    # input the image name from spy for encoding
    original_image = raw_input("What is the name of image?")
    # name spy wants to give to encoded image
    output_path = raw_input("What is the name of output image")
    # secret text spy wants to send to selected friend
    text = raw_input("What do you want to say??")
    # encoding the image
    Steganography.encode(original_image, output_path, text)
    # saving the details of message through 'Chat_Message' class
    new_chat = Chat_Message(text, True, 0, 0)
    # appending the chat in 'chats' list of selected friend
    friends[friend_choice].chats.append(new_chat)
    print colored("Your secret message has been sent!!!!", 'blue')

# Function to read a message
def read_message():
    # saying the spy to select friend whose chat want to read
    friend_choice = select_friend()
    # name of image from which message has to be retrieved
    output_path = raw_input("What is the name of file u want to read message?")
    # decoding the image and storing the text
    text = Steganography.decode(output_path)
    # testing whether there is message in image or not
    if len(text) > 0:
        # Checking the no of words in a message if more than 100 remove that friend
        if len(text.split()) > 100:
            print colored("You are spamming the chat..that' s why u  are removed from spy's friend list", 'red')
            del(friends[friend_choice])
        else:
            no_of_words = len(text.split())
            # If not more than 100 save that chat in chat list
            new_chat = Chat_Message(text, False, friend_choice, no_of_words)
            friends[friend_choice].chats.append(new_chat)
            print colored("Your secret message has been saved", 'blue')
            print colored("Average  no of words spoken by spy's friend %d" % friends[friend_choice].average, 'blue')
            # List of special words
            special_words = ["SOS", "SAVE ME", "HELP", "DANGER"]
            # If there is special word in message print appropriate message
            for word in text.upper().split():
                if word in special_words:
                    print colored("Mission Compromised....as our spy is in danger....please help our spy!!!!!", 'red')
    else:
        # If no message in image warn the spy
        print colored("The image contain no secret message", 'red')

# Function to read chat history
def chat_history():
    # selecting the friend from spy with whom old chat wants to read
    read_for = select_friend()
    # Checking if there is old chat with selected friend if yes show the old chat
    if len(friends[read_for].chats) > 0:
        for chat in friends[read_for].chats:
            # If the chat from spy side
            if chat.sent_by_me:
                print"[%s] %s %s" % (chat.time.strftime(colored("%d/%B/%Y", 'blue')),
                                     colored('You said:', 'red'), chat.message)
            # If chat from friend side
            elif not chat.sent_by_me:
                print"[%s] %s" % (chat.time.strftime(colored("%d/%B/%Y", 'blue')),
                                  colored(friends[read_for].name, 'red')) + colored(" said:", 'red') + chat.message
    # If there is no old chat with selected friend
    else:
        print colored(" There is no previous chat with this user", 'red')

# Function to add a friend
def add_friend():
    new_friend = Spy('', 0, 0.0, False)
    # Input from spy the name and salutation of friend
    new_friend.name = raw_input("Enter friend name")
    # Checking the validity of name by calling 'valid_name' and passing the name as argument
    if valid_name(new_friend.name):
        # If name is valid...input salutation for friend
        new_friend.name = raw_input("Are they (Mr./Ms./Dr.)?") + new_friend.name
        # Welcome message for friend
        print colored("Welcome %s" % new_friend.name, 'blue')
        # Input friends age
        new_friend.age = int(raw_input("Enter friend's age?"))
        # Checking eligibility of  friend to be a spy or not
        if valid_age(new_friend.age):
            print colored("%s is eligible to be a spy" % new_friend.name, 'blue')
            # If eligible...enter friend's rating
            new_friend.rating = float(raw_input("Enter friend's rating?"))
            # Friend's rating should be greater than spy's rating
            if new_friend.rating >= spy.rating:
                print colored("You are eligible to be spy's friend", 'blue')
                # Input friend online status
                new_friend.is_Online = raw_input("Is Your Friend Online(True/False)")
                # Appending new friend in 'friends' list
                friends.append(new_friend)
                print colored("Your friend is added to ur list", 'blue')
            else:
                # If rating is less......friend can't be added in list
                print colored("Your rating is not up to criteria", 'red')
        else:
            # If age is not meeting the criteria....friend can't be a spy
            print colored("Your friend %s is not eligible to be a spy" % new_friend.name, 'red')
    else:
        # If name is not valid
        print colored("Your friend name is invalid", 'red')
    # Returning no of friends in 'friends' list
    return len(friends)

# defining function for adding status
def add_status(current_status_message):
    # Checking if current status is 'None or not'..If not print current status
    if current_status_message is not None:
        print colored("Your Current status message is %s\n" % current_status_message, 'blue')
    else:
        # If None.....print appropriate message
        print colored("You don't have any status message currently\n", 'red')
    new_status_message = None
    # Asking the spy whether spy will select from older status or add new status
    default = raw_input("Do you want to select from the older status(Y/N)?")
    # If not from older status then ask the spy which new status want to set
    if default.upper() == "N":
        new_status_message = raw_input("What status do you want to set?")
        # Checking if new status is not empty then append in 'status_message' list
        if len(new_status_message) > 0:
            status_message.append(new_status_message)
            # new status will be returned
            return new_status_message
    # If from older status then show the older status
    elif default.upper() == "Y":
        for j in range(len(status_message)):
            print"%d . %s" % (j+1, status_message[j])
            # Ask the spy to select from above list by selecting index of status
        selection = int(raw_input("\nChoose from the above list of status"))
        # Checking if the index input by spy is <= the no. of status in status_message list..
        # If true then set that status as new status
        if len(status_message) >= selection:
            new_status_message = status_message[selection-1]
            # new status will be returned
            return new_status_message
        # If not 'warn the spy'
        else:
            print colored("You entered a wrong index", 'red')
    # If spy enter other than 'y or n' then show this message
    else:
        print colored("The option you entered is not valid! please enter y or n", 'red')


# defining a function for chat
def start_chat(spy):
    show_menu = True
    print colored("Welcome to spy chat", 'blue')
    while show_menu:
        # Showing  the choices to spy until spy chooses to close application
        menu_choices = int(raw_input("What do you want to do?\n"
                                     " 1. Add a status update\n "
                                     "2. Add Friend\n "
                                     "3. send message\n"
                                     " 4. read message\n "
                                     "5. Read chats from a user\n "
                                     "6. Close application"))
        # Spy wants to update status
        if menu_choices == 1:
            print colored("You choose to update", 'blue')
            # Calling 'add_status' to update status
            spy.current_status_message = add_status(spy.current_status_message)
            # Printing the new status returned by 'add_status'
            print colored("Your new status is %s" % spy.current_status_message, 'blue')
        # Spy wants to enter a new friend
        elif menu_choices == 2:
            # Calling 'add_friend' to add details of friend
            no_of_friends = add_friend()
            # Print no of friends returned by 'add_friend'
            print colored("You have %d friends" % no_of_friends, 'blue')
        # Spy wants to send message to friend
        elif menu_choices == 3:
            # calling 'send_message' function
            send_message()
        # Spy wants to read message from friend
        elif menu_choices == 4:
            # Calling 'read_message' function
            read_message()
        # Spy wants to read old chat with friend
        elif menu_choices == 5:
            # Calling 'chat_history' function
            chat_history()
        # Spy wants to close application
        elif menu_choices == 6:
            show_menu = False
            print colored("Closing Application...\n Closed", 'blue')
        # Spy has entered wrong choice
        else:
            print colored("Enter valid entry from the menu", 'red')

# defining function for details
def details():
    # Creating the object of 'Spy' class with none values in it
    spy = Spy('', 0, 0.0, '')
    # Input from spy...name
    spy.name = raw_input("What is ur name?")
    # Checking the correctness of name
    if valid_name(spy.name):
        # # If name is correct....ask the spy about salutation
        spy.name = raw_input("What should we call u?(Mr./Ms./Dr.)") + spy.name
        # Print welcome message for spy
        print colored("Hello! %s" % spy.name, 'blue')
        # Input spy's age
        spy.age = int(raw_input("What is ur age?"))
        # Validating spy's age to be spy or not
        if valid_age(spy.age):
            #  If valid  input spy's rating
            print colored("You are eligible to be a spy", 'blue')
            spy.rating = float(raw_input("What is ur rating?"))
            # Informing the spy about category on the basis of rating
            rating_criteria(spy.rating)
            # setting spy's online status
            spy.is_online = True
            # After all checks print message with all details of spy
            print colored("Authentication complete...Spy Name=%s, Spy Age=%d, Spy Rating=%.2f, Spy Status=%s"
                          % (spy.name.title(), spy.age, spy.rating, spy.is_online), 'blue')
            # calling start_chat() function to start  the chat
            start_chat(spy)
        else:
            # If spy's age is not according to criteria
            print colored("You are not eligible", 'red')
    else:
        # If spy enter invalid name
        print colored("Invalid Name", 'red')

# give our user the option to continue with default user  or define a new user
question = raw_input("continue as  %s (Y/N)" % spy.name)
# checking the input
if question.upper() == "Y":
    # if user continues with same details calling start_chat() function to start the chat
    start_chat(spy)
elif question.upper() == "N":
    # if not continues with same details calling details() function to add new details
    details()
# If Spy enter other than "y/n"
else:
    print colored("You entered a wrong choice!!!", 'red')
