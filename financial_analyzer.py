import re

def extract_financials(text):

    data = {
        "revenue": 0,
        "profit": 0,
        "debt": 0,
        "assets": 0
    }

    revenue = re.search(r"Revenue\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    profit = re.search(r"Profit\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    debt = re.search(r"Debt\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    assets = re.search(r"Assets\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)

    if revenue:
        data["revenue"] = int(revenue.group(1).replace(",", ""))

    if profit:
        data["profit"] = int(profit.group(1).replace(",", ""))

    if debt:
        data["debt"] = int(debt.group(1).replace(",", ""))

    if assets:
        data["assets"] = int(assets.group(1).replace(",", ""))

    return data
