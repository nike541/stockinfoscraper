import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://www.moneycontrol.com/"


reponse = requests.get(url)

soup = BeautifulSoup(reponse.content,"html.parser")

nifty50 = soup.find("div",class_ ="marActnBx")

sensex = soup.find("div",class_ = "indices_Sensex")

print(nifty50)
print(sensex)
#nifty50_value = nifty50.text.strip()
#sensex_value = sensex.text.strip()

#data = { 
#    "Index" : ["Nifty_50" , "Sensex"],
#    "Value" : [nifty50_value, sensex_value]
#}

#df = pd.DataFrame(data)
#print(df)

#csv_file_path = "financial_data.csv"

#df.to_csv(csv_file_path,index=False)

#print(f"Data has been saved to {csv_file_path}")




