import os # Os to clear the console from clutter
import time as t # Time to delay console changes
from tabulate import tabulate as tab # Used to create a well-formatted manner console printed table
import numpy_financial as npf # Collection of elementary financial functions used for computing payment against loan principal plus interest.
from datetime import datetime # To get current day
import pandas as pd # For data framing and access
import math 

# Avoid scientific notation
pd.set_option("display.float_format", "{:,.2f}".format)

# Reusable function for clearing the console
def clear(seconds):
    t.sleep(seconds) # This is to indicate how long will it take before clearing
    os.system('cls' if os.name == 'nt' else 'clear') # Clear console statement


# Function to display funds in a formatted table
def show_funds(fund_type, funds_df, day):
    display_df = funds_df.copy()
    display_df["Stock Price"] = display_df["Stock Price"].astype(float)

    # Calculate market cap
    display_df["Market Cap"] = display_df["Stock Price"] * display_df["Outstanding Shares"]

    # Format columns to avoid scientific notation and add commas
    display_df["Outstanding Shares"] = display_df["Outstanding Shares"].apply(lambda x: f"{x:,}")
    display_df["Market Cap"] = display_df["Market Cap"].apply(lambda x: f"{x:,.2f}")

    # Only keep clean columns
    display_df = display_df[["Company", "Stock Price", "Outstanding Shares", "Market Cap"]]
    display_df = display_df.reset_index(drop=True)
    display_df.index += 1  

    # Display the table
    print(f"\n{fund_type} Funds (Prices as of {day}):\n")
    print(tab(display_df, headers="keys", tablefmt="github"))
    print


# Function to handle investment session for a selected fund type
def invest_session(funds_arr):
    while True:
        print("\nEnter the number of the company you want to invest in: ")
        choice_company = input("Enter choice: ")
        if choice_company.isdigit() and 1 <= int(choice_company) <= len(funds_arr):
            break
        print("Invalid choice. Please try again.\n")
        
    company_choice = funds_arr.iloc[int(choice_company) - 1]
    print(f"\nYou have chosen to invest in {company_choice['Company']}")
    
    amount = float(input("Enter amount to invest: ₱ "))
    print(f"\nProcessing your investment of ₱{amount:,} in {company_choice['Company']}...")
    
    # Simulate investment processing
    t.sleep(2)
    print("Investment processed successfully!\n")
    print(f"You have purchased \033[1;37m{math.floor(amount / company_choice['Stock Price']):,} shares\033[0m of {company_choice['Company']} at ₱{company_choice['Stock Price']:.2f} per share.")
    
    input("\nPress Enter to continue...")
    clear(2)
    
        
# Function for investing in Philippine Stock Exchange
def invest_in_pse():
    today = datetime.today()
    day = today.strftime("%A") # Get the current day of the week

    # For simulating changes in stock prices
    days = {
        "Monday": 1.23,
        "Tuesday": 1.45,
        "Wednesday": 1.67,
        "Thursday": 0.89,
        "Friday": 1.11,
        "Saturday": 1.33,
        "Sunday": 1.55
    }
    
    multiplier = days[day]

    # Create companies data list
    # 0 for renewable funds, 1 for gaming funds, 2 for utility funds, 3 for mining funds
    companies_data = [
        ["AC Energy (ACEN)", 2.22 * multiplier, 39677394773, None, 0],
        ["First Gen Corp. (FGEN)", 16.4 * multiplier, 50073050000, None, 0],
        ["Solar Philippines (SPNEC)", 1.3 * multiplier, 3596575505, None, 0],
        ["Digi Plus Interactive Corp. (PLUS)", 23 * multiplier, 4507493678, None, 1],
        ["Bloomberg Resorts Corp. (BLOOM)", 3.1 * multiplier, 11487534908, None, 1],
        ["PhilWeb Corp. (WEB)", 3.22 * multiplier, 1435776680, None, 1],
        ["Manila Electric Company (MER)", 535 * multiplier, 1127092509, None, 2],
        ["Aboitiz Power Corp. (AP)", 42.4 * multiplier, 7205854307, None, 2],
        ["Manila Water Company Inc. (MWC)", 42 * multiplier, 2601499272, None, 2],
        ["Nickel Asia Corp. (NIKL)", 2.79 * multiplier, 13931125094, None, 3],
        ["Apex Mining Company Inc. (APX)", 6.76 * multiplier, 6227887491, None, 3],
        ["Philex Mining Corporation (PX)", 6.65 * multiplier, 5782399068, None, 3]
    ]

    # Format into DataFrame with headers
    dataframe = pd.DataFrame(companies_data, columns=["Company", "Stock Price", "Outstanding Shares", "Market Cap", "Fund Type"])

    # Separate dataframes for each fund type
    renewable_funds = dataframe[dataframe["Fund Type"] == 0]
    gaming_funds = dataframe[dataframe["Fund Type"] == 1]
    utility_funds = dataframe[dataframe["Fund Type"] == 2]
    mining_funds = dataframe[dataframe["Fund Type"] == 3]

    # Calculation for market cap
    dataframe["Market Cap"] = dataframe["Stock Price"] * dataframe["Outstanding Shares"]

    # Fund type selection
    print("\n\tSelect Fund Type")
    print("[1] Renewable Energy")
    print("[2] Gaming")
    print("[3] Utilities")
    print("[4] Mining")
    print("[5] Go back")

    choice = input("\nEnter choice: ")

    if choice == "1":
        show_funds("Renewable Energy", renewable_funds, day)
        invest_session(renewable_funds)
        
    elif choice == "2":
        show_funds("Gaming", gaming_funds, day)
        invest_session(gaming_funds)
        
    elif choice == "3":
        show_funds("Utilities", utility_funds, day)
        invest_session(utility_funds)

    elif choice == "4":
        show_funds("Mining", mining_funds, day)
        invest_session(mining_funds)
    
    elif choice == "5":
        clear(1)

    else:
        print("Invalid choice")

    clear(1)


# Function to obtain a loan and display amortization schedule
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

# Main program side
clear(1)
# Credentials input
print("\n\tLOGIN")
username = input("Enter username: ")
password = input("Enter password: ")
logged_in = False

# Loops while the credentials are wrong
while not logged_in:
    if username == "fintech2026" and password == "admin123":
        logged_in = True
        print("\nLogin successful!")
        clear(1)
        
    else:
        print("\n\033[31mLogin failed. Please try again.\033[0m")
        clear(1.5)
        username = input("Enter username: ")
        password = input("Enter password: ")

print("\nWelcome to Fintech console app!")

# Main transaction loop after login
while logged_in:
    print("\n\tSelect a transaction")
    t.sleep(.5)
    print("[1] Invest in PSE Fund")
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