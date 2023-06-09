import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "T5U6TJH39V577HD0"
NEWS_API_KEY = "0d0599b55ee04b7398ab4e8e878a3d87"

account_sid = "ACd1450229cdb2f6e9f98edd8baf45f814"
auth_token = "0d0c9e359199d0196a5062b015e04908"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": "IBM",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
data_list = [value for (key, value) in data.items()]
yesterdays_closing_price = data_list[1]["2023-06-08"]["4. close"]
print(yesterdays_closing_price)

last_weeks_closing_price = data_list[1]["2023-06-02"]["4. close"]
print(last_weeks_closing_price)

difference = abs(float(yesterdays_closing_price) - float(last_weeks_closing_price))
print(difference)


diff_percent = (difference / float(yesterdays_closing_price)) * 100
print(diff_percent)

news_params = {
    "q": "IBM",
    "apiKey": NEWS_API_KEY
}
if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": "IBM"

    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"HeadLine: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+13614597365',
            to='+233263976829'
        )

        print(message.sid)


