import random

def calculate_risk(text):

    # simple demo risk score
    score = random.randint(50, 90)

    if score > 75:
        level = "Low Risk"
    elif score > 60:
        level = "Moderate Risk"
    else:
        level = "High Risk"

    return score, level