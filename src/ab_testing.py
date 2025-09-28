import pandas as pd
from scipy import stats

def ab_test(df, campaign1, campaign2):
    group1 = df[campaign1]
    group2 = df[campaign2]
    stat, pval = stats.ttest_ind(group1, group2)
    return stat, pval

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_marketing_data.csv")
    stat, pval = ab_test(df, 'AcceptedCmp1', 'AcceptedCmp2')
    print(f"T-stat: {stat}, P-value: {pval}")
