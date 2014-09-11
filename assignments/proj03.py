#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 12-Aug-2014
    Project No: 3"""
#================================================================

# Calculate gallon of water used
def gallons_used(start_meter, end_meter):
    if end_meter > start_meter:
        gallons_ = (end_meter-start_meter)/10.0
    else:
        gallons_ = (999999999-start_meter + end_meter + 1)/10.0
    return gallons_

# Calculate the amount for customer
def calculate_rate(customer_code, gallons_in_use):

    liter_in_use = gallons_in_use*3.8
    one_million = 10**6

    if customer_code == 'r':
        # if the customer code is r
        rate_customer = 5.00 + liter_in_use*.0005

    elif customer_code == 'c':
        #If the customer code is c then check the below conditions
        if (liter_in_use < (4 * one_million)) | (liter_in_use == (4 * one_million)):
            rate_customer = 1000.00
        elif liter_in_use > (4*one_million):
            rate_customer = 1000.00 + (liter_in_use-(4*one_million))*0.00025

    elif customer_code == 'i':
        # if the customer code is i the check the below conditions
        if liter_in_use < (4 * one_million):
            rate_customer = 1000.00
        elif (liter_in_use > (4*one_million)) & (liter_in_use < 10**7):
            rate_customer = 2000.00
        elif liter_in_use > 10**7:
            rate_customer = 2000.00 + (liter_in_use-10**7)*(2000+.00025)
    else:
        rate_customer = 0


    return rate_customer


def final_customer_report(customer_code, start_meter, end_meter, gallons,amount):
    print '\nCustomer Code:', customer_code
    print 'Beginning meter reading:', start_meter
    print 'Ending meter reading:', end_meter
    print 'Gallons of water used', gallons
    print 'Amount Billed:', '$'+str(amount)


# Main Program
while True:
    print '\n'
    # Input customer code
    customer_code = raw_input('Enter customer code:')

    #Accept only if customer code is r ,c or i
    if (customer_code == 'r') | (customer_code == 'c') | (customer_code == 'i'):
        #Enter start meter reading
        start_meter = input('Enter beginning meter reading:')
        # Enter end meter reading
        end_meter = input('Enter ending meter reading:')
        # Calculate gallons used
        gallons_in_use = gallons_used(start_meter, end_meter)
        # Calculate the amount for customers
        customer_rate = calculate_rate(customer_code, gallons_in_use)
        # Print final customer details
        final_customer_report(customer_code, start_meter, end_meter, gallons_in_use, customer_rate)
    else:
        break
