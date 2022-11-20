import datetime
import requests

api_key = 'w8RTJy8IQ6OCRV5foAvD69xaTicGnnIw'


def currency_period_days(days=365):
    date_today = datetime.date.today()
    period_to_365 = date_today - datetime.timedelta(days=days)

    url = f"https://api.apilayer.com/currency_data/timeframe?start_date={period_to_365}&end_date={date_today}&source=EUR&currencies=RUB"

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()
    return result


if __name__ == '__main__':
    print(currency_period_days())
