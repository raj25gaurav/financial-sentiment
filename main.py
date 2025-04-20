from flask import Flask, request, jsonify
from app.fetch_news import fetch_news
from app.preprocess import clean_text
from app.sentiment_model import analyze_sentiment
from app.aggregator import aggregate
from app.config import FINNHUB_API_KEY

app = Flask(__name__)

@app.route('/sentiment', methods=['GET'])
def sentiment():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Please provide a ticker symbol"}), 400
    
    raw_news = fetch_news(ticker, FINNHUB_API_KEY)
    if not raw_news:
        return jsonify({"error": "No news found"}), 404

    cleaned = [clean_text(h) for h in raw_news]
    sentiments = [analyze_sentiment(h) for h in cleaned]
    result = aggregate(sentiments)

    return jsonify({
        "ticker": ticker,
        "news_count": len(raw_news),
        "sentiment": result
    })

if __name__ == '__main__':
    app.run(debug=True)