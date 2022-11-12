import requests
result = "1"
url = "https://www.fast2sms.com/dev/bulkV2"
querystring = {
    "authorization":"pHygw5Gkd9XemIV7YUENWDTcPtfBA8ihrJKj02CZuaqQvR36LFAhFTatkgpGyDfEPlcqJoNuLYeSz4MH",
        "sender_id":"DR-PREDICTION",
        "message":"Results: "+ result,
        "language":"english",
        "route":"q",
        "numbers": "9500680243, 6385357372"
    }
headers = {
        'cache-control': "no-cache"
    }

    
print(querystring)
res = requests.request("GET",url,headers=headers,params=querystring)
print(res.text)