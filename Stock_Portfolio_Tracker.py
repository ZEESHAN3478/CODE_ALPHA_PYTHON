# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("📈 Stock Portfolio Tracker")

# User input for stocks
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("❌ Stock not found in list!")

# Calculate total investment
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock} : {quantity} shares × ${price} = ${value}")

print("\n💰 Total Investment Value:", total_value)

# Save result to file
save = input("Do you want to save result to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        file.write(f"{stock} : {quantity} shares × ${price} = ${value}\n")

    file.write(f"\nTotal Investment Value: {total_value}")
    file.close()

    print("✅ Data saved to portfolio.txt")

print("Program Finished.")