import requests

base = "USD"
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/B?format=json")
print(response.status_code)
if response.ok == True:
    data = response.json()
    jsono=data[0]
    rates = jsono["rates"]
    for rate in rates:
        print(rate['currency'],rate['mid'])
    # base = data["table"]
    # date = data["effectiveDate"]

    # print("base: " + base)
    # print("date: " + date)
    # #print(rates)
    #
    # for key in rates:
    #     print(key + ": ", rates[key])

