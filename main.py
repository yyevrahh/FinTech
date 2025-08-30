import os # Os to clear the console from clutter
import time as t # Time to delay console changes
from tabulate import tabulate as tab # Used to create a well-formatted manner console printed table
import numpy_financial as npf # Collection of elementary financial functions used for computing payment against loan principal plus interest.

# Reusable function for clearing the console
def clear(seconds):
    t.sleep(seconds) # This is to indicate how long will it take before clearing
    os.system('cls' if os.name == 'nt' else 'clear') # Clear console statement


# Function for investing in Philippine Stock Exchange
def invest_in_pse():
    
    # Dictionaries for different fund types
    renewable_funds = {
        "AC Energy (ACEN)": 2.22,
        "First Gen Corp. (FGEN)": 16.4,
        "Solar Philippines (SPNEC)": 1.3
    }
    
    gaming_funds = {
        "Digi Plus Interactive Corp. (PLUS)": 23,
        "Bloomberg Resorts Corp. (BLOOM)": 3.1,
        "PhilWeb Corp. (WEB)": 3.22
    }
    
    utility_funds = {
        "Manila Electric Company (MER)": 535,
        "Aboitiz Power Corp. (AP)": 42.4,
        "Manila Water Company Inc. (MWC)": 42
    }
    
    mining_funds = {
        "Nickel Asia Corp. (NIKL)": 2.79,
        "Apex Mining Company Inc. (APX)": 6.76,
        "Philex Mining Corporation (PX)": 6.65
    }

    # Fund type selection
    print("\n\tSelect Fund Type")
    print("[1] Renewable Energy")
    print("[2] Gaming")
    print("[3] Utilities")
    print("[4] Mining\n")
    fund_choice = input("Enter choice: ")

    if fund_choice == "1":
        funds = renewable_funds
        fund_type = "Renewable Energy"
    elif fund_choice == "2":
        funds = gaming_funds
        fund_type = "Gaming"
    elif fund_choice == "3":
        funds = utility_funds
        fund_type = "Utilities"
    elif fund_choice == "4":
        funds = mining_funds
        fund_type = "Mining"
    else:
        print("Invalid choice")
        return

    clear(1)
    


def obtain_loan():
    print("\n\tObtain a loan")
    amount = float(input("Enter loan amount: ₱ "))
    
    print("\n\tChoose the tenor")
    print("[1] 6 months (8%)")
    print("[2] 1 year (7.5%)")
    print("[3] 2 years (7%)")
    print("[4] 3 years (6.5%)")
    print("[5] 4 years (6%)")
    print("[6] 5 years (5%)\n")
    
    tenor_choice = input("Enter choice: ")

    if tenor_choice == "1":
        tenor = 6
        interest_rate = 0.08
        
    elif tenor_choice == "2":
        tenor = 12
        interest_rate = 0.075
        
    elif tenor_choice == "3":
        tenor = 24
        interest_rate = 0.07
        
    elif tenor_choice == "4":
        tenor = 36
        interest_rate = 0.065
        
    elif tenor_choice == "5":
        tenor = 48
        interest_rate = 0.06
        
    elif tenor_choice == "6":
        tenor = 60
        interest_rate = 0.05
    else:
        print("Invalid choice")
        return

    print("Generating amortization schedule...")
    clear(1.5)

    # Calculate monthly payment using interest rate (per month), total months (tenor), and loan amount going out
    monthly_payment = npf.pmt(interest_rate / 12, tenor, -amount)
    
    # Show the monthly payment
    print(f"\nMonthly payment for ₱{amount} over {tenor} months is: ₱{monthly_payment:.2f}")

    # Placeholders for amortization schedule
    months = []
    principals = []
    interests = []
    balances = []
    
    balance = amount
    rate = interest_rate / 12 # Divide into months

    for month in range(1, tenor + 1): # As in for every month selected

        # Calculate interest, principal, and balance
        interest = balance * rate
        principal = monthly_payment - interest
        balance -= principal

        # Append each values to the lists
        months.append(month)
        principals.append(principal)
        interests.append(interest)
        balances.append(max(0.0, balance))

    # List for tabulated rows
    rows = []
    
    # Combine each month’s principal, interest, and balance into a row
    for m, p, i, b in zip(months, principals, interests, balances):
        rows.append([m, f"₱{p:,.2f}", f"₱{i:,.2f}", f"₱{b:,.2f}"])


    # Display the amortization table using the tabulate library 
    headers = ["Month", "Principal", "Interest", "Balance"]
    print("\nAmortization Schedule:\n")
    print(tab(rows, headers=headers, tablefmt="github"))
    

    # Wait for user to finish viewing
    input("\nPress Enter to continue...")
    clear(2)


# Function for paying utility bills
def pay_util_bills():
    print("\n\tSelect a merchant\n")
    print("[1] Manila Water")
    print("[2] Meralco")
    print("[3] PLDT")
    print("[4] Globe Telecom")
    print("[5] Converge")
    print("[6] DITO Telecom\n")

    choice = input("Enter choice: ")
    print()

    if choice == "1":
        print("You selected Manila Water")

    elif choice == "2":
        print("You selected Meralco")

    elif choice == "3":
        print("You selected PLDT")

    elif choice == "4":
        print("You selected Globe Telecom")

    elif choice == "5":
        print("You selected Converge")

    elif choice == "6":
        print("You selected DITO Telecom")

    else:
        print("Invalid choice")
        return

    contract_number = input("Enter contract number: ")
    amount = input("Enter amount to pay: ₱ ")

    print(f"Processing payment for ₱{amount} on contract {contract_number}...")
    t.sleep(2)
    print("Payment successful!")
    clear(1.5)


# Credentials input
print("\n\tLOGIN")
username = input("Enter username: ")
password = input("Enter password: ")
logged_in = False

# Loops while the credentials are wrong
while not logged_in:
    if username == "fintech2026" and password == "admin123":
        logged_in = True
        print("Login successful!")
        clear(1)
        
    else:
        print("Login failed. Please try again.")
        clear(1.5)
        username = input("Enter username: ")
        password = input("Enter password: ")

print("\nWelcome to Fintech console app!")

while logged_in:
    print("\n\tSelect a transaction")
    t.sleep(.5)
    print("[1] Invest in PSE Fund \033[31m(NOT AVAILABLE)\033[0m")
    print("[2] Obtain a loan")
    print("[3] Pay Utility Bills")
    print("[4] Logout\n")

    choice = input("Enter choice: ")
    clear(1) # Clear previous console
    
    if choice == "1":
        invest_in_pse()
    
    elif choice == "2":
        obtain_loan()
        
    elif choice == "3":
        pay_util_bills()
        
    elif choice == "4":
        print("Logging out...")
        clear(1)
        logged_in = False
        
    else:
        print() # Adds a space
        print("Invalid choice. Please try again.")
        clear(1.5)