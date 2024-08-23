import requests
api_key="5ee13abcd4-665b5f02fc-si7d90"
currencyFrom=str(input("Enter what type of currency you want to convert: "))
CurrencyTo=str(input("Enter type of currency : "))
amount=float(input("Enter amount of money you want to convert: "))
url=f"https://api.fastforex.io/fetch-one?from={currencyFrom}&to={CurrencyTo}&api_key={api_key}"
response=requests.get(url)
print(response.status_code)
temp=response.json()['result']
print(f'{amount} from {currencyFrom} to {CurrencyTo} is {temp}')