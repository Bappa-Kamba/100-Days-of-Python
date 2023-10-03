import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "FA6TRRHM970W9PQO"
NEWS_API_KEY = "e8a1d4a03d324a19b4ebe030e2629ec7"

app_sid = "ACe5e3ea080e39568c29e146f1301bc9ff"
auth_token = "af803bc9a667355c6e80125c226a3b53"

client = Client(app_sid, auth_token)

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

stock_data = data["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
# yesterday's close
previous_close = float(stock_data_list[0]['4. close'])
# day before yesterday's close
previous_previous_close = float(stock_data_list[1]['4. close'])
difference = round(previous_close - previous_previous_close, 2)
diff_percent = round((abs(difference) / previous_close) * 100, 2)

if abs(diff_percent) > 1:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_params = {
        "q" : COMPANY_NAME,
        "searchIn" : 'title',
        "language" : "en",
        "sortBy" : "publishedAt",
        "apiKey" : NEWS_API_KEY,
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    articles = news_response.json()['articles']
    top_3_articles = articles[:3]
    
    if difference < 0:
        title = f"{STOCK}: 🔻{diff_percent}%"
    else:
        title = f"{STOCK}: 🔺{diff_percent}%"

    for news_article in top_3_articles:
        stock_news = f"{title}\nHeadline: {news_article['title']}\nBrief: {news_article['description']}"


        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number. 
        message = client.messages.create(
                                    body=stock_news,
                                    from_='whatsapp:+14155238886',
                                    to='whatsapp:+2348136384068'
                                )
        print(message.sid)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

