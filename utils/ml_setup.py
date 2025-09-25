import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

def load_campaign_data(db_path='genAI-marketing-tool.db'):
    connect = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM campaigns", connect)
    return df

def prepare_data(df):
    df['CTR'] = df['clicks'] / df['impressions']

    X = df[['impressions', 'clicks', 'CTR']]
    y = df['conversions']
    return X, y


def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

if __name__ == "__main__":
    df = load_campaign_data()
    X, y = prepare_data(df)
    model = train_model(X, y)
    print("Model trained successfully.")
    print(f"Coefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_}")
