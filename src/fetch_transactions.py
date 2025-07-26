import os
import requests
import pandas as pd
import time
from dotenv import load_dotenv

load_dotenv()
COVALENT_API_KEY = os.getenv("COVALENT_API_KEY")

CHAIN_ID =os.getenv("CHAIN_ID")

def get_compound_transactions(wallet_address):
    url = f"https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet_address}/transactions_v2/"
    params = {"key": COVALENT_API_KEY}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data.get("data") is None:
        print(f"No data for {wallet_address}")
        return pd.DataFrame()

    txs = data["data"]["items"]
    df = pd.json_normalize(txs)
    return df
# wallet_df = pd.read_csv("data/Wallet_Ids.csv")  
# wallets = wallet_df['wallet_id'].tolist()
# all_data = []


# for wallet in wallets:
#     print(f"Fetching data for: {wallet}")
#     df = get_compound_transactions(wallet)
#     if not df.empty:
#         df['wallet'] = wallet 
#         time.sleep(1.5)
#         all_data.append(df)


# if all_data:
#     combined_df = pd.concat(all_data, ignore_index=True)
#     print(combined_df.head())
#     print(combined_df.info())
#     combined_df.to_csv("results/fetched_transactions.csv", index=False)
# else:
#     print("No data fetched.")
