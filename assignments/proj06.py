#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 13-Aug-2014
    Project No: 6"""
#================================================================

# Validate for the user inputs
def validate(command, index, str_change):

    valid = True
    validate_message = ''

    # If command is add check if the index is out of range
    if command == 'a':
        if len(str_change) < index:
            validate_message = 'Error: Index out of range'
            valid = False

    # If command is to delete then characters other than - cannot be deleted
    if command == 'd':
        s = str_change[index:index+1]
        if s != '-':
            validate_message = 'Error: You cannot delete a character that is not indel'
            valid = False

    valid_ = [valid, validate_message]
    return valid_

# Compare the final changed strings to count the similarities , dissimilarities.
# Make the similar ones with lower case and dissimilar ones with upper case.
def score_report(change_first, change_second):
    similarity_count = 0
    dissimilarity_count = 0
    new_first = ''
    new_second = ''

    # Looping through each word in the strings and counting and changing the case
    for a, b in zip(change_first, change_second):
        if a == b:
            similarity_count += 1
            new_first += a.lower()
            new_second += b.lower()
        else:
            dissimilarity_count += 1
            new_first += a.upper()
            new_second += b.upper()

    report = [similarity_count, dissimilarity_count, new_first, new_second]
    return report

#  Input the first sequence
first_string = raw_input('Enter the First Sequence:')
# Input the second sequence
second_string = raw_input('Enter the Second Sequence:')
change_first = first_string
change_second = second_string

# Print the initial command message
print '''Please select on of the below commands
        "a" for add. Add an Indel
        "d" for delete.Delete an Indel
        "s" for score.Score the Present alignment
        "q" for quit.Stop the process.'''

while True:
    # Select the user command
    command = raw_input('\nSelect command:')

    # If command is to add then do the following
    if command == 'a':
        # Select which string to change and index to place the Indel (-)
        string_change = input('\tEnter which string to change (1 or 2):')
        index = input('\tIndex at which you wish to place the Indel:')

        if string_change == 1:
            par = change_first
        else:
            par = change_second
        # Validate user input
        valid = validate(command, index, par)

        if valid[0]:
            # If valid user input then do the following
            if string_change == 1:
                change_first = change_first[:index] + '-' + change_first[index:]
                print '\tFirst Sequence:', change_first
                print '\tSecond Sequence:', change_second
            else:
                change_second = change_second[:index] + '-' + change_second[index:]
                print '\tFirst Sequence:', change_first
                print '\tSecond Sequence:', change_second
        else:
            #Else print error message
            print valid[1]

    # If command is to delete then do the following
    elif command == 'd':
        # Select which string to change and index to delete the Indel (-)
        string_change = input('\tEnter which string to change (1 or 2):')
        index = input('\tIndex at which you wish to delete the Indel:')

        if string_change == 1:
            par = change_first
        else:
            par = change_second
        # Validate user input
        valid = validate(command, index, par)

        if valid[0]:
            # If valid user input then do the following
            if string_change == 1:
                change_first = change_first[:index]+change_first[index+1:]
                print '\tFirst Sequence:', change_first
                print '\tSecond Sequence:', change_second
            else:
                change_second = change_second[:index]+change_second[index+1:]
                print '\tFirst Sequence:', change_first
                print '\tSecond Sequence:', change_second
        else:
            # Else print error message
            print valid[1]

    # If the command is score do the following
    elif command == 's':
        len_first = len(change_first)
        len_second = len(change_second)

        # Add '-' to the end to make the length of two sequences equal
        if len_first != len_second:
            if len_first > len_second:
                change_second += '-' * (len_first-len_second)
            else:
                change_first += '-' * (len_second-len_first)

        #total_similarities = sum(a == b for a, b in zip(change_first, change_second))
        #total_disimilarities = sum(a != b for a, b in zip(change_first, change_second))
        # Calculate the score report
        report = score_report(change_first,change_second)

        #Print the score report
        print '\n\tSimilarities:', report[0]
        print '\tDissimilarities:', report[1]
        print '\tFirst String:', report[2]
        print '\tSecond String:', report[3]

    # If command is quit , quit from the loop
    elif command == 'q':
        break
