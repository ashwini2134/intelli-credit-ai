def extract_financial_features(text):

    features = {}

    features["revenue"] = text.count("revenue")
    features["loan"] = text.count("loan")
    features["debt"] = text.count("debt")

    return features