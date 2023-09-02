import requests
from twilio.rest import Client

account_sid = 'ACb11594d29dcb561abc33f736a3debb9b'
auth_token = '9be17d632dbe39cc1df1710137c87555'

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=8QNX98RWQJ09TM1P'

r = requests.get(url)
data = r.json()["Time Series (Digital Currency Daily)"]["2023-09-02"]

# print(data)

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

data_0901 = r.json()["Time Series (Digital Currency Daily)"]["2023-09-01"]
close_usd_0901 = float(data_0901["4b. close (USD)"])

data_0831 = r.json()["Time Series (Digital Currency Daily)"]["2023-08-31"]
close_usd_0831 = float(data_0831["4b. close (USD)"])

ratio = round((((close_usd_0831 - close_usd_0901) / close_usd_0831) * 100), 2)
# print(ratio)

if abs(ratio) > 5:
    print("Get news")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

url = ('https://newsapi.org/v2/everything?q=Bitcoin&from=2023-09-01&sortBy=popularity&apiKey=323b35a87c734fe596c29dcd1e069924')

response = requests.get(url)

news_lists = response.json()["articles"]

news_popular = []
for news in range(0, 3):
    news_popular.append(news_lists[news]["title"])
    news_popular.append(news_lists[news]["description"])

# print(news_popular[0])
# print(news_popular[1])

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"Bitcoin : {ratio}\n"
         f"{news_popular[0]}\n"
         f"{news_popular[1]}",
    from_='+12563051618',
    to='+886960063863'
)

print(message.status)

# Optional: Format the SMS message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or

"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""
