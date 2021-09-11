import requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=YOUR_API_KEY")
print(r.text)
print(r.status_code)

url = "www.something.com"
data = {
    "one":"1",
    "two" : "2"
}

r2 = requests.post(url=url,data=data)
print(r2.text)
print(r2.status_code)