#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 31-Aug-2014
    Project No:8"""
#================================================================

# Initialize variables
sum = 0
natural_palindrome = []
non_lychrel = []
lychrel = []
delimiter = ','
lychrel_range = 60

# To get the from range
from_num = input("Check from:")
# Get the to range
to_num = input("Check up to:")

# To get the palindromes , lychrel and non-lychrel numbers
for p in range(from_num, to_num+1):
    number = str(p)
    rev_number = number[::-1]
    # Check if the number is natural palindrome
    if number == rev_number:
        natural_palindrome.append(number)

    else:
        # Check if the number is non-lychrel or lychrel number
        sum = int(number) + int(rev_number)
        for i in range(0, lychrel_range):
            if str(sum) == str(sum)[::-1]:
                non_lychrel.append(number)
                break
            sum += int(str(sum)[::-1])
            if (i == lychrel_range-1) & (str(sum) != str(sum)[::-1]):
                lychrel.append(number)

# Print values of Natural Palindromes, non-lychrel and lychrel numbers
print "Number of Natural Palindromes = " + str(len(natural_palindrome))
print "Natural Palindrome numbers: " + delimiter.join(natural_palindrome)
print "Number of non-lychrel numbers = " + str(len(non_lychrel))
print "Non lychrel numbers: " + delimiter.join(non_lychrel)
print "Number of lychrel numbers = " + str(len(lychrel))
print "Lychrel numbers: " + delimiter.join(lychrel)
