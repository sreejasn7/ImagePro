#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 12-Aug-2014
    Project No: 4"""
#================================================================

# Input the order for the square
order = input('Please input the order of the square:')
# Input the top left number
top_num = input('Please input the top left number:')
# The latin square is
print 'The Latin Square is:'

order += 1
# To loop for each row
for i in range(1, order):
    # To loop for each column
    for j in range(1, order):

        # Check if the number is equal to the order
        if top_num != (order-1):
            print top_num,
            top_num += 1
        else:
            print top_num,
            top_num = 1

    if top_num != (order-1):
        top_num += 1
    else:
        top_num = 1
    print '\n'