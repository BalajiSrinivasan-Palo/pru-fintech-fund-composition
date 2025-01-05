import random
from datetime import datetime
import sys

# Fixed tickers for fund composition
all_tickers = ["SHOP.TRT","RELIANCE.BSE", "GPV.TRV", "IBM"]

# Generate random proportions for each fund
def generate_fund_compositions(fund_names, date):
    compositions = {}
    for fund in fund_names:
        proportions = [random.random() for _ in all_tickers]
        total = sum(proportions)
        normalized_proportions = [p / total for p in proportions]
        compositions[fund] = {
            "date": date,
            "positions": [
                {"ticker": ticker, "proportion": proportion}
                for ticker, proportion in zip(all_tickers, normalized_proportions)
            ]
        }
    return compositions

# Example usage
fund_names = ["Fund A", "Fund B"]
date = datetime.now().strftime("%Y-%m-%d")
fund_compositions = generate_fund_compositions(fund_names, date)
print(fund_compositions)