def generate_cam(score, level):

    if level == "Low Risk":
        decision = "Loan Approved"
    elif level == "Moderate Risk":
        decision = "Approve with Conditions"
    else:
        decision = "Loan Rejected"

    cam_report = f"""
    CREDIT APPRAISAL MEMO

    Risk Score: {score}
    Risk Level: {level}

    Recommendation:
    {decision}

    Interest Rate: 10%
    Loan Tenure: 5 Years
    """

    return cam_report