def get_retention_strategy(probability):

    if probability >= 0.80:

        return [
            "High Churn Risk",
            "Assign Dedicated Relationship Manager",
            "Offer Premium Loyalty Discount",
            "Provide Free Data Booster",
            "Prioritize Complaint Resolution"
        ]

    elif probability >= 0.60:

        return [
            "Medium Churn Risk",
            "Offer Retention Promotion",
            "Provide Bonus Data Benefits",
            "Recommend Better Plan"
        ]

    elif probability >= 0.40:

        return [
            "Moderate Churn Risk",
            "Send Personalized Offers",
            "Increase Customer Engagement"
        ]

    else:

        return [
            "Low Churn Risk",
            "Maintain Regular Customer Engagement"
        ]