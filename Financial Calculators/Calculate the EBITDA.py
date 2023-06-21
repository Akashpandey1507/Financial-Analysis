'''--------------------------------Calculate the EBITDA---------------------------------'''

def Calculate_EBITDA():

    # Need Net Income
    Net_Income = float(input('Enter the Net Income: '))
    # Need Interest
    Interest = float(input('Enter the Net Interest: '))
    # Need Taxes
    Taxes = float(input('Enter the Net Tax: '))
    # Need Depriciation
    Depriciation = float(input('Enter the Net Depriciation: '))
    # Need Amortization
    Amortization = float(input('Enter the Net Amortization: '))

    # Formula for calculating EBITDA
    EBITDA = round(Net_Income + Interest + Taxes + Depriciation + Amortization)

    # Print the Resut
    return (f'The EBITDA is :Rs. {EBITDA}')


print(Calculate_EBITDA())
