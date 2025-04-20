def aggregate(sentiment_list):
    pos, neg, neu = 0, 0, 0
    n = len(sentiment_list)
    for s in sentiment_list:
        pos += s['positive']
        neg += s['negative']
        neu += s['neutral']
    
    avg = {
        "average_positive": round(pos/n, 4),
        "average_negative": round(neg/n, 4),
        "average_neutral": round(neu/n, 4),
    }

    if max(avg.values()) == avg['average_positive']:
        avg["overall_sentiment"] = "positive"
    elif max(avg.values()) == avg['average_negative']:
        avg["overall_sentiment"] = "negative"
    else:
        avg["overall_sentiment"] = "neutral"
    return avg