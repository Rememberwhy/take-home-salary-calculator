def get_country():
    # Dictionary to store the list of countries and their corresponding numbers
    countries = {
        "1": "United States",
        "2": "United Kingdom",
        "3": "Canada",
        "4": "China"
    }
    
    # Print out the list of countries for the user to choose from
    print("Select your country:")
    for key, value in countries.items():
        print(f"{key}. {value}")
    
    # Loop until a valid choice is made
    while True:
        choice = input("Enter the number corresponding to your country: ")
        if choice in countries:
            return countries[choice]
        else:
            print("Invalid choice. Please select a valid country number.")

def calculate_tax_us(income):
    """Calculate tax for the United States based on progressive tax rates."""
    if income <= 9875:
        return income * 0.10
    elif income <= 40125:
        return 987.5 + (income - 9875) * 0.12
    elif income <= 85525:
        return 4617.5 + (income - 40125) * 0.22
    elif income <= 163300:
        return 14605.5 + (income - 85525) * 0.24
    elif income <= 207350:
        return 33271.5 + (income - 163300) * 0.32
    elif income <= 518400:
        return 47367.5 + (income - 207350) * 0.35
    else:
        return 156235 + (income - 518400) * 0.37

def calculate_tax_uk(income):
    """Calculate tax for the United Kingdom based on progressive tax rates."""
    if income <= 12500:
        return 0
    elif income <= 50000:
        return (income - 12500) * 0.20
    elif income <= 150000:
        return 7500 + (income - 50000) * 0.40
    else:
        return 47500 + (income - 150000) * 0.45

def calculate_tax_ca(income):
    """Calculate tax for Canada based on progressive tax rates."""
    if income <= 48535:
        return income * 0.15
    elif income <= 97069:
        return 7280.25 + (income - 48535) * 0.205
    elif income <= 150473:
        return 17229.72 + (income - 97069) * 0.26
    elif income <= 214368:
        return 31114.76 + (income - 150473) * 0.29
    else:
        return 49644.31 + (income - 214368) * 0.33

def calculate_tax_cn(income):
    """Calculate tax for China based on progressive tax rates."""
    if income <= 36000:
        return income * 0.03
    elif income <= 144000:
        return 1080 + (income - 36000) * 0.1
    elif income <= 300000:
        return 10800 + (income - 144000) * 0.2
    elif income <= 420000:
        return 34800 + (income - 300000) * 0.25
    elif income <= 660000:
        return 61800 + (income - 420000) * 0.3
    elif income <= 960000:
        return 120000 + (income - 660000) * 0.35
    else:
        return 210000 + (income - 960000) * 0.45

def get_tax(country, income):
    """Get the appropriate tax calculation function based on the selected country."""
    if country == "United States":
        return calculate_tax_us(income)
    elif country == "United Kingdom":
        return calculate_tax_uk(income)
    elif country == "Canada":
        return calculate_tax_ca(income)
    elif country == "China":
        return calculate_tax_cn(income)
    else:
        return income * 0.20  # Default flat tax rate

def calculate_take_home_salary():
    """Calculate and display the take-home salary based on user inputs."""
    country = get_country()
    print(f"You selected: {country}")
    
    income = int(input("Put your annual income before tax here: "))
    
    tax = get_tax(country, income)
    
    insurance = int(input("Enter your annual insurance amount here: "))
    
    expenses = int(input("Enter all other annual expenses you have: "))
    
    take_home = income - tax - insurance - expenses
    
    print("\n" + "="*50)
    print(f"Country: {country}")
    print(f"Annual Income: {income:,}")
    print(f"Annual Tax: {tax:,}")
    print(f"Annual Insurance: {insurance:,}")
    print(f"Annual Expenses: {expenses:,}")
    print(f"Take Home Salary: {take_home:,}")
    print("="*50 + "\n")

def main():
    """Main function to drive the application."""
    while True:
        calculate_take_home_salary()
        another = input("Would you like to check another amount or another country? (yes to continue, done to exit): ")
        if another.lower() == "done":
            print("You exited from the application. Have a good day!")
            break

if __name__ == "__main__":
    main()
