def get_retention_strategy(probability):

    if probability >= 0.80:
        return [
            "Offer premium loyalty discount",
            "Assign dedicated customer support",
            "Provide free data package"
        ]

    elif probability >= 0.50:
        return [
            "Offer retention promotion",
            "Provide bonus data benefits",
            "Send personalized offers"
        ]

    else:
        return [
            "Customer is low churn risk"
        ]