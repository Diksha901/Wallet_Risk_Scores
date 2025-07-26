**Aim of the Project** : 
* Fetch transaction history for a given wallet id.
* Engineer features to get meaningful insights from the data
* Develop a scoring model to get `Risk Score` of the wallet using engineered features .

---

**Files in this Repository** 

----->*src/*

      ------------> feature_engineering.py 
      ------------> fetch_transactions.py
      ------------> main.py 
      ------------> scoring_model.py
      
----->*results/*

      ------------> feature_score.csv 
      ------------> final_scores.csv
      ------------> final_scores_ml.csv
      
----->*notebooks/*

      ------------> analysis.ipynb
      
----->*data/*

      ------------> Wallet_Ids.csv
      
----->*requirements.txt* 

---


**Data Collection** : I have got the data of transactions(v2 endpoint) related to each wallet by using Covalent API Key(v1 version) and Chain id (a unique identifier of a blockchain network) 
in `fetch_transactions.py`  
**Features Selection** : According to the fetched data , the important features can be 
1. activity days : Few active daya will signify more risk .
2. gas_spent : Higher gas spent means high activity ( maybe low risk)
3. total_transactions : Fewer transactions may mean more risky
4. avg_value (Average Transaction value) : Lower the average value , higher the risk
5. max_value : High value of transactions may imply some risky bet .
  > I have got these in my `feature_engineering.py`


**Scoring Model** :  I have used a weighted formula to get risk score in `scoring_model.py`: `risk = 0.2 * (1 / (1 + features['activity_days'])) + 0.3 * (1 / (1 + features['avg_value'])) +/
           0.3 * (1 / (1 + features['total_tx'])) + /
           0.2 * (1 / (1 + features['gas_spent']))`
> A weight of 0.2 is given to activity days and gas_spent while we take the features avg_value and total_tx(transactions) as more important features(weights=0.3) .
> A high value of each of the following features will imply a lower risk and vice-a-versa .
> we have also trained a Random Forest regressor to get risk_scores from the features engineered . But the ML trained model does not give good results . Due to high percentage of high risk wallets most scores are towards 1000 in final_ml_scores.csv.
> Heuristic based weighted formula in `scoring_model.py` works better than ML model for this case . 
   
