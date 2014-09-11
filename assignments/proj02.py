#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 11-Aug-2014
    Project No: 2"""
#================================================================

# Define a function to print message
def message():
    return '''This is a puzzle favoured by Einstein.You will be asked to enter a 3 digit number,
where the hundred's digit differs from the one's digit by at least two.The procedure will always yield 1089'''

#Print Message
print message()
#Input a number
number = input('Give me a number:')
#Reverse number
reverse_num = int(str(number)[::-1])
# Calculate the difference
difference = abs(number-reverse_num)
# Reverse the difference
reverse_diff = int(str(difference)[::-1])
#Print the reverse number
print 'For the number:', number, 'the reverse number is:', reverse_num
#Print the difference
print 'The difference between {} and {} is'.format(number, reverse_num), difference
#Print the reverse of difference
print 'The reverse difference is:', reverse_diff
# Calculate the sum of difference and reverse of difference
print 'The sum of {} and revDiff is'.format(difference, reverse_diff), difference+reverse_diff