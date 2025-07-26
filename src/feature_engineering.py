import pandas as pd

def generate_features(df):
    if df.empty:
        return {}

    total_tx = len(df)
    gas_spent = pd.to_numeric(df['fees_paid'],errors='coerce').sum() if 'fees_paid' in df else 0
    avg_value = pd.to_numeric(df['value'],errors='coerce').mean()
    max_value = pd.to_numeric(df['value'],errors='coerce').max()

    
    df['block_signed_at'] = pd.to_datetime(df['block_signed_at'])
    activity_days = (df['block_signed_at'].max() - df['block_signed_at'].min()).days

    features = {
        "total_tx": total_tx,
        "gas_spent": gas_spent,
        "avg_value": avg_value,
        "max_value": max_value,
        "activity_days": activity_days
    }
    return features
