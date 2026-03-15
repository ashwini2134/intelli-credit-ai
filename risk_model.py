def calculate_risk(text, financials):

    score = 50

    revenue = financials.get("revenue")
    profit = financials.get("profit")
    debt = financials.get("debt")
    assets = financials.get("assets")

    try:
        if revenue:
            revenue = int(revenue.replace(",", ""))
        if profit:
            profit = int(profit.replace(",", ""))
        if debt:
            debt = int(debt.replace(",", ""))
        if assets:
            assets = int(assets.replace(",", ""))
    except:
        pass

    # Profit increases score
    if profit and profit > 0:
        score += 15

    # Revenue strength
    if revenue and revenue > 1000000:
        score += 10

    # Debt ratio
    if debt and assets:
        ratio = debt / assets

        if ratio > 0.7:
            score -= 20
        elif ratio > 0.4:
            score -= 10

    # Risk level
    if score >= 70:
        level = "Low Risk"
    elif score >= 50:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return score, level