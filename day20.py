# # requests
# import requests
# url = "https://www.onlinekhabar.com/smtm/search-list/tickers"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json()['response']
#     for result in data:
#         if result['sector'] == "Microfinance":
#             print(result['ticker_name'])
#         # continue



# r = requests.get(url=url, verify=False)



f = open('day19.py','r')
data = f.read()



# f = open('day21.py','w')
# f.write("hello ")
# f.close()


f = open('day21.py','a')
f.write("a = 100\t")
f.close()