#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 2-Sep-2014
    Project No:9"""
#================================================================
import re
import math

# Regular expression setting
roman_re = re.compile("""^
   ([M]{0,9})   # thousands
   ([DCM]*)     # hundreds
   ([XLC]*)     # tens
   ([IVX]*)     # units
   $""", re.VERBOSE)

# Decimal to roman table
dec2rmn_table = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M','MM', 'MMM']]


# Convert roman to decimal
def roman_to_numeral(roman):
    roman = roman.upper()
    match = roman_re.match(roman)
    thousands, hundreds, tens, units = match.groups()
    result = 1000 * len(thousands)
    result += dec2rmn_table[2].index(hundreds) * 100
    result += dec2rmn_table[1].index(tens) * 10
    result += dec2rmn_table[0].index(units)

    return result

# Convert decimal to roman
def numeral_to_roman(numeral):
    result = str()
    len_numeral = len(numeral)
    for i in range(0, len_numeral):
        result += str(dec2rmn_table[len_numeral-i-1][int(numeral[i])])
    return result


# Enter the roman numerals
first_roman = raw_input("Enter first roman numeral: ")
second_roman = raw_input("Enter second roman numeral: ")
# Convert roman to numeral
first_numerals = roman_to_numeral(first_roman)
# Convert roman to numeral
second_numerals = roman_to_numeral(second_roman)
# Calculate the sum
sum_numerals = int(first_numerals) + int(second_numerals)
# Convert number to roman numeral
print numeral_to_roman(str(sum_numerals))

