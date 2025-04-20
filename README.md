
# Condor Financial Sentiment Analysis

## Project Description
This project aims to build an end-to-end solution for financial sentiment analysis using news data. The system retrieves financial news articles, processes them, applies a pre-trained sentiment analysis model, and exposes the results via a REST API. This prototype is designed for the Condor AI Engineer Take-Home Assignment.

### Key Components:
1. **Data Ingestion**: Fetching financial news data from APIs like Financial Modeling Prep or Alpha Vantage.
2. **Data Preprocessing**: Cleaning and tokenizing the news data for further analysis.
3. **Sentiment Analysis**: Using a pre-trained model (DistilBERT or FinBERT) to classify news sentiment (positive, negative, or neutral).
4. **API Development**: Exposing the sentiment analysis through a REST API built with Flask.
5. **Containerization**: Packaging the solution with Docker to ensure portability and ease of deployment.

## Project Structure
```
condor-financial-sentiment/
│
├── app/
│   ├── __init__.py
│   ├── sentiment.py           # Sentiment analysis logic
│   └── utils.py               # Helper functions for data ingestion and processing
│
├── data/
│   ├── news_data.csv          # Example of stored news data (optional)
│
├── Dockerfile                 # Docker configuration for the containerized solution
├── requirements.txt           # List of dependencies
├── .gitignore                 # Files and directories to ignore
├── README.md                 # Project documentation
└── run.py                     # Script to run the application
```

## Setup and Execution Instructions

### Prerequisites
- Python 3.8+
- Docker (optional, for containerization)
- Git

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/condor-financial-sentiment.git
   cd condor-financial-sentiment
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scriptsctivate'
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python run.py
   ```
   The application should now be running locally on `http://localhost:5000`.

### API Endpoint

- **Endpoint**: `/sentiment`
- **Method**: GET
- **Parameters**: 
   - `ticker` (string): The stock ticker (e.g., "AAPL" for Apple).
- **Response**: 
   - JSON object containing the aggregated sentiment of recent news for the specified ticker.

Example:
```bash
curl "http://localhost:5000/sentiment?ticker=AAPL"
```

### How to Test the API

1. Start the application using the command above.
2. Use `curl` or Postman to send a GET request to the `/sentiment` endpoint.
3. The response will be a JSON object with a sentiment classification for the requested financial entity.

## Assumptions and Design Choices

1. **Model Choice**: I have chosen `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face for sentiment analysis due to its strong performance on text classification tasks and efficiency in handling large amounts of text data.
2. **News Data Source**: I used **Financial Modeling Prep** for retrieving the latest news articles. This choice was made based on their accessible API and financial coverage.
3. **Sentiment Aggregation**: The sentiment for each financial entity is aggregated by taking the most frequent sentiment label from the processed news articles.
4. **Containerization**: Docker was used to ensure that the application can be easily deployed in different environments.

## Future Improvements

1. **Enhance Sentiment Model**: Consider fine-tuning a model like FinBERT for more accurate financial sentiment analysis, as it's specialized for financial contexts.
2. **Extend News Sources**: Integrate additional news sources for broader coverage and more robust sentiment analysis.
3. **Real-time Updates**: Introduce real-time data fetching and sentiment analysis to provide up-to-date results.
4. **Error Handling**: Improve error handling in API and data processing steps to provide more robust production-ready code.

## License
This project is licensed under the MIT License.

