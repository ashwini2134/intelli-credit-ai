def loan_decision(score):

    if score > 70:
        return "Loan Rejected"
    elif score > 40:
        return "Review Required"
    else:
        return "Loan Approved"