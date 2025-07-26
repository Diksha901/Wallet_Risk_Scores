import pandas as pd
from fetch_transactions import get_compound_transactions
from feature_engineering import generate_features
from scoring_model import risk_score

wallet_df = pd.read_csv("data/Wallet_Ids.csv")  
wallets = wallet_df['wallet_id'].tolist()
all_data = []


results = []

for wallet in wallets:
    print(f"Processing wallet: {wallet}")
    df = get_compound_transactions(wallet)
    features = generate_features(df)
    if features:
        score = risk_score(features)
        features['wallet'] = wallet
        features['risk_score'] = score
        results.append(features)


df_result = pd.DataFrame(results)
df_result.to_csv("results/features_scores.csv", index=False)
print("Done! Scores saved to features_scores.csv")
score_df=pd.DataFrame(wallets,df_result['risk_score'])
score_df.to_csv("results/final_scores.csv")

