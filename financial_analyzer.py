import re

def extract_financials(text):

    data = {
        "revenue": None,
        "profit": None,
        "debt": None,
        "assets": None
    }

    revenue = re.search(r"Revenue\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    profit = re.search(r"Profit\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    debt = re.search(r"Debt\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)
    assets = re.search(r"Assets\s*[:\-]?\s*([\d,]+)", text, re.IGNORECASE)

    if revenue:
        data["revenue"] = revenue.group(1)

    if profit:
        data["profit"] = profit.group(1)

    if debt:
        data["debt"] = debt.group(1)

    if assets:
        data["assets"] = assets.group(1)

    return data