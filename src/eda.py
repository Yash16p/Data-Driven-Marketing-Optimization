import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def eda(df):
    print(df.describe())
    sns.histplot(df['Age'], bins=20, kde=True)
    plt.title("Age Distribution")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_marketing_data.csv")
    eda(df)
