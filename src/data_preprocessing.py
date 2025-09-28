import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Drop NA
    df = df.dropna()
    # Example: Create Age column
    if 'Year_Birth' in df.columns:
        df['Age'] = 2025 - df['Year_Birth']
    return df

if __name__ == "__main__":
    df = load_data("data/marketing_data.csv")
    df_clean = clean_data(df)
    df_clean.to_csv("data/cleaned_marketing_data.csv", index=False)
    print("✅ Data cleaned and saved!")
