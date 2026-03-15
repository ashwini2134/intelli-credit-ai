def calculate_risk(text, financials):

    score = 50

    # Convert values safely to integers
    revenue = int(financials.get("revenue") or 0)
    profit = int(financials.get("profit") or 0)
    debt = int(financials.get("debt") or 0)
    assets = int(financials.get("assets") or 1)

    # Prevent division by zero
    if assets == 0:
        assets = 1

    # Profit condition
    if profit > 0:
        score += 15

    # Revenue condition
    if revenue > 1000000:
        score += 10

    # Debt ratio calculation
    debt_ratio = debt / assets

    if debt_ratio > 0.7:
        score -= 20
    elif debt_ratio > 0.4:
        score -= 10

    # Risk level classification
    if score >= 70:
        level = "Low Risk"
    elif score >= 50:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return score, level
