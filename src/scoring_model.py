from sklearn.preprocessing import MinMaxScaler
import numpy as np

def risk_score(features: dict):
    
    risk = 0.2 * (1 / (1 + features['activity_days'])) + \
           0.3 * (1 / (1 + features['avg_value'])) + \
           0.3 * (1 / (1 + features['total_tx'])) + \
           0.2 * (1 / (1 + features['gas_spent']))

    score = 1000 * (1 - min(risk, 1))
    return np.round(score, 2)
