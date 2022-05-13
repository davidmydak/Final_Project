import requests
import json
from datetime import date

n = input("Give me name of wanted currency and date(in format yyyy-mm-dd) : ").split()
if len(n) > 1:
    base, date = n
    url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"
    payload = {}
    headers = {"apikey": "0RPGb1E88jiJ0p44uXbG0V6btGF1NH1B"}
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code != 200:
        print(f"Invalid date: {date}")
        exit()
    JSON = json.loads(response.text)
    base_responce = JSON["base"]
    data_responce = JSON["date"]
    value = JSON["rates"]["UAH"]

    print(f"{base_responce}\n{value}")
else:
    base= n[0]
    date = date.today()
    url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"
    payload = {}
    headers = {"apikey": "0RPGb1E88jiJ0p44uXbG0V6btGF1NH1B"}
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code != 200:
        print(f"Invalid base: {base}")
        exit()
    JSON = json.loads(response.text)
    base_responce = JSON["base"]
    value = JSON["rates"]["UAH"]
    print(f"{base_responce} \n{value}")

