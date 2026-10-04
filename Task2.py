# Stock Portfolio Tracker
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Number of different stocks
n = int(input("\nHow many stocks do you want to add? "))

for i in range(n):
    stock = input(f"\nEnter stock symbol #{i + 1}: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        portfolio[stock] = quantity

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: {quantity} × ${stock_prices[stock]} = ${investment}")
    else:
        print("Stock not found in the price list.")

# Display summary
print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares → ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== Stock Portfolio =====\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(
                f"{stock}: {quantity} shares → ${value}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment}")

    print("Portfolio saved successfully to portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker! 📊")
