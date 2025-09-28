import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

def build_model(df):
    X = df[['Age', 'Income']]  # adjust features later
    y = df['Response']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))
    print("AUC:", roc_auc_score(y_test, preds))

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_marketing_data.csv")
    build_model(df)
  