import pandas, requests
import pandas as pd
import numpy as np


url = "https://marketdata.tradermade.com/api/v1/live"

currency = "USDJPY,GBPUSD,UK100"
api_key = "hA0rnbkmszpDUsWDLgnS"

##################################################################
#querystring = {"currency":currency,"api_key":api_key}
#response = requests.get(url, params=querystring)


#df = pd.DataFrame(response.json()["quotes"])
#print(df)



##############################################################
#url = "https://marketdata.tradermade.com/api/v1/live"

#currency = "USDJPY,GBPUSD,UK100"
#api_key = "hA0rnbkmszpDUsWDLgnS"
#querystring = {"currency":currency,"api_key":api_key}

#response = requests.get(url, params=querystring)

#print(response.json())

####################################################################
#querystring = {"currency":currency,"api_key":api_key}
#response = requests.get(url, params=querystring)
#df = pd.DataFrame(response.json()["quotes"])
#df["instrument"] = np.where(df["base_currency"].isnull(),df["instrument"],df["base_currency"]+df["quote_currency"])
#df["instrument"] = df["base_currency"]+df["quote_currency"]
#df["timestamp"] = response.json()["timestamp"]
#df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
#print(df)

####################################################################
#querystring = {"currency":currency,"api_key":api_key}
#response = requests.get(url, params=querystring)
#df = pd.DataFrame(response.json()["quotes"])
#df["instrument"] = np.where(df["base_currency"].isnull(),df["instrument"],df["base_currency"]+df["quote_currency"])
#df["instrument"] = df["base_currency"]+df["quote_currency"]
#print(df)

###################################################################
currency = ["EURUSD"]
querystring = {"currency":currency,"api_key":api_key}
response = requests.get(url, params=querystring)
df = pd.DataFrame(response.json()["quotes"])

currency = ["USDJPY"]
querystring = {"currency":currency,"api_key":api_key}
response = requests.get(url, params=querystring)
da = pd.DataFrame(response.json()["quotes"])
print(df)
print(da)
print(currency)


#############################################################
#url = "https://marketdata.tradermade.com/api/v1/historical"
#date = "2021-03-15"
#querystring = {"currency":currency,"date":date, "api_key":api_key}
#response = requests.get(url, params=querystring)
#df = pd.DataFrame.from_dict(response.json()["quotes"], orient='columns', dtype=None, columns=None)
#df["instrument"] = np.where(df["base_currency"].isnull(),df["instrument"],df["base_currency"]+df["quote_currency"])
#df["date"] = response.json()["date"]
#df["date"] = pd.to_datetime(df["date"])
#print(df)


#############################################################
#fx = ["EURUSD", "USDJPY"]
#dates = ["2021-03-15-13:00"]
#array = []
#url = "https://marketdata.tradermade.com/api/v1/minute_historical"
#for i in fx:
#	for date in dates: 
#		querystring = {"currency":i,"date_time":date, "api_key":api_key}
#		response = requests.get(url, params=querystring)
#		array.append(response.json())
#df = pd.DataFrame(array)
#print(df)


###################################################################

#url = "https://marketdata.tradermade.com/api/v1/timeseries?"
#currency="EURUSD"
#start_date="2021-03-01"
#end_date="2021-03-22"
#format="split"
#interval="daily"

#df =pd.read_json('https://marketdata.tradermade.com/api/v1/timeseries?currency='
#	+currency+'&api_key='+api_key+'&start_date='+start_date+'&end_date='
#	+end_date+'&format='+format+'&interval='+interval)
#df = pd.DataFrame(df.quotes['data'], columns=df.quotes['columns'])
#forex_trade = df.tail() 
# or forex_trade = df
#print(forex_trade)
#print(currency)

########################################################################

