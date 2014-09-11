#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 31-Aug-2014
    Project No: 7"""
#================================================================
import getpass
import sys
from collections import Counter

# Initialize values
counter = 12
history = []

# Check if the user input is valid
def valid_user_input(user_key):

    word_count = Counter(user_key).values()
    word_count.sort(reverse=True)
    valid = False
    error_msg = ''

    # Check for the length of the guessed key
    if len(user_key) != 4:
        error_msg = 'Error: Entered key should contain 4 digits'
    elif not str(user_key).isdigit():
        # Check the entered key contains all numbers
        error_msg = 'Error: Characters not acceptable'
    elif word_count[0] > 1:
        # Check if the numbers are repeated or not
        error_msg = 'Error: Numbers cannot be repeated'
    else:
        valid = True

    print error_msg

    return valid

# Give messages related to positions of the guess relative to key
def check_guess(guess, key):
    a = key.find(guess[i])
    b = guess.find(key[a])
    a += 1
    b += 1
    count = 0
    if a:
        if a == b:
            print '\tOne number exactly correct (' + guess[i] + ')'

        if a != b:
            print '\t' + str(i+1) + ' number in the wrong position (' + guess[i] + ')'

    else:
        count = 1

    return count

# Input the key
if sys.stdin.isatty():
    key = getpass.getpass('Please enter the key:')
else:
    print 'Using Read Line'
    key = sys.stdin.readline().rstrip()

# Main Program
while counter:

    # Print previous guessed history
    if len(history) != 0:
        print "\nYour previous history was"+ str(history[:])
        print "You got "+str(counter)+" more chances"

    guess = raw_input('\nAny Guess? ')
    len_guess = len(guess)

    # If user input is valid then check if the geess matches with the key value
    if valid_user_input(guess):

        history.append(guess)
        full_string = key.find(guess)
        full_string += 1

        # If the guess is correct
        if full_string:
            print "***************************You won the game****************************"
            exit()
        else:
            # if the guess is not correct then check for each number in the guess.
            count = 0
            for i in range(0, len_guess):
                count += check_guess(guess, key)
                if count == len_guess: print "Guess completely wrong"
    else:
        counter += 1

    # Decrement the counter value
    counter -= 1
    # If guess is wrong even at the 12th round then print lost message
    if counter == 0:
        print "\n**************Sorry!!!!!! You lost the game******************************** \nThe key is " + key