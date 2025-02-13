import requests
from twilio.rest import Client
from datetime import datetime,timedelta
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
def get_closing_price(stock_name):
    stock_api = "https://www.alphavantage.co/query"
    stock_api_key = "TO778HQCEI8VU1WZ"
    request = requests.get(stock_api, params={
                                'function': 'TIME_SERIES_DAILY',
                                'apikey': stock_api_key,
                                'symbol':stock_name})
    data = request.json()
    time_series = data['Time Series (Daily)']
    data_list=[n for n in time_series.items()]
    d0_data=data_list[0]
    d1_data = data_list[1]
    return_data={
        "D0": {
            "date":d0_data[0],
            "data":d0_data[1]
        },
        "D1":{
            "date":d1_data[0],
            "data":d1_data[1]
        }
    }

    return return_data
#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company_name):
    news_api = "https://newsapi.org/v2/everything"
    news_api_key = "ccaa3879ce794482892ac943945f21ee"
    news_api_params={"apiKey": news_api_key,
                     "q":company_name,
                     "sortBy": "publishedAt"}
    news_response = requests.get(news_api, params=news_api_params).json()
    news_list=news_response['articles']

    return news_list[0:3]

def send_sms_notification(message):
    account_sid = 'AC93de7bcd904c80a1b17474e2c7bfa1d0'
    auth_token = 'd1d68290f0698d32c43f679be3de39e1'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG18e357cd6901aa14be928a520b533856',
        body= message,
        to='+6583992760'
    )
    print(message.sid)

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.




#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

price_list=get_closing_price(STOCK_NAME)
D0_Close=float(price_list["D0"]["data"]["4. close"])
D1_Close=float(price_list["D1"]["data"]["4. close"])
price_diff= D0_Close - D1_Close
percent_change = (abs(price_diff) / D0_Close)*100
if percent_change>5:
    news= get_news(COMPANY_NAME)
    news_str= [f"{COMPANY_NAME}:{"🔺" if price_diff>0 else "🔻"}{percent_change}%\nHeadline:{n["title"]}\nBrief:{n["description"]}" for n in news]
    for n in news_str:
        send_sms_notification(n)
    #print(n)
