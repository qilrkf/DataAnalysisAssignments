import pandas as pd

def load_data():
    df0 = pd.read_csv('superstore.csv', encoding='windows-1252')
    df = df0[['Profit', 'Sales', 'Quantity', 'Discount']]
    df = df.rename(columns={'Sales': 'Sales_amount'})
    return df
