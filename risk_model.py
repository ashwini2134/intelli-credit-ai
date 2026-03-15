def calculate_risk(text, financials):

    score = 50

    revenue = financials.get("revenue", 0)
    profit = financials.get("profit", 0)
    debt = financials.get("debt", 0)
    assets = financials.get("assets", 1)

    if profit > 0:
        score += 15

    if revenue > 1000000:
        score += 10

    debt_ratio = debt / assets

    if debt_ratio > 0.7:
        score -= 20
    elif debt_ratio > 0.4:
        score -= 10

    if score >= 70:
        level = "Low Risk"
    elif score >= 50:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return score, level