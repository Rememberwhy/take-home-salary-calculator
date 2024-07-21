income = int(input("Put your income before tax here: "))

tax = income * 0.2

insurance = int(input("Enter your insurance amount here: "))

expanses = int(input("Enter all other expanses you have: "))

take_home = income - insurance - expanses - tax

print("Your money after all the spend is: ", take_home)
