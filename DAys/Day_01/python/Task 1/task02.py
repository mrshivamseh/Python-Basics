# 1. Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 2800
}

# 2. User input for portfolio
portfolio = {}
n = int(input("Kitne stocks add karna chahte ho? "))

for i in range(n):
    stock = input("Stock symbol (e.g., AAPL, TSLA): ").upper()
    qty = int(input(f"Quantity of {stock}: "))
    portfolio[stock] = qty

# 3. Calculate total investment
total_value = 0
for stock, qty in portfolio.items():
    if stock in stock_prices:
        total_value += stock_prices[stock] * qty
    else:
        print(f"⚠️ Price not available for {stock}")

print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    if stock in stock_prices:
        print(f"{stock} - {qty} shares @ {stock_prices[stock]} USD")

print(f"\n💰 Total Investment Value: {total_value} USD")

# 4. Optional: Save result to file
save = input("Do you want to save result to file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        f.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            if stock in stock_prices:
                f.write(f"{stock} - {qty} shares @ {stock_prices[stock]} USD\n")
        f.write(f"\nTotal Investment Value: {total_value} USD\n")
    print("✅ Portfolio saved to portfolio.txt")
