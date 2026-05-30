import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    return df