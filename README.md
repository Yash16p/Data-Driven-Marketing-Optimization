# 📊 Marketing Campaign Optimization using Data Science

## 📌 Project Overview
This project analyzes customer marketing campaign data to **optimize targeting, improve conversion rates, and reduce customer acquisition costs (CAC)**.  
We apply **data analysis, visualization, statistical testing, and machine learning** to uncover insights and recommend data-driven marketing strategies.

---

## 🎯 Objectives
- Define and track **key performance indicators (KPIs)** such as Conversion Rate, CAC, CLV, and ROI.  
- Perform **exploratory data analysis (EDA)** to understand customer behavior and campaign response patterns.  
- Conduct **A/B testing** to compare marketing campaigns statistically.  
- Build a **predictive model** to forecast customer responses.  
- Design an **interactive dashboard** in Tableau/Google Data Studio for business stakeholders.  
- Deliver **actionable insights** with a professional report.

---

## 🗂️ Project Structure
```

marketing-optimization-ds/
│── data/                     # Raw + processed datasets
│   ├── marketing_data.csv
│   └── cleaned_marketing_data.csv
│
│── notebooks/                # Jupyter notebooks for analysis
│   ├── 01_data_cleaning.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_AB_testing.ipynb
│   └── 04_modeling.ipynb
│
│── src/                      # Python scripts (modular code)
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── ab_testing.py
│   ├── modeling.py
│   └── utils.py
│
│── reports/                  # Final outputs
│   ├── figures/              # Graphs & visuals
│   └── Marketing_Report.pdf
│
│── dashboards/               # Tableau / Google Data Studio files or links
│   └── dashboard_notes.txt
│
│── requirements.txt          # Python dependencies
│── README.md                 # Project overview
│── .gitignore

````

---

## 🛠️ Tech Stack
- **Languages & Libraries:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SciPy  
- **Visualization Tools:** Tableau, Google Data Studio, Excel, Google Sheets  
- **Experimentation:** Hypothesis Testing, A/B Testing, Statistical Modeling  
- **Machine Learning:** Logistic Regression, Random Forest  
- **Others:** Git, Jupyter Notebooks, VS Code  

---

## 📊 Workflow

### 1️⃣ Data Preparation
- Load dataset (`marketing_data.csv`)  
- Handle missing values, duplicates, outliers  
- Feature engineering: Age, Income bins, Campaign success indicators  

### 2️⃣ KPI Definition
- Conversion Rate = Accepted Offers / Total Customers  
- Customer Acquisition Cost (CAC)  
- Customer Lifetime Value (CLV)  
- ROI by campaign  

### 3️⃣ Exploratory Data Analysis (EDA)
- Age, Income, Spending habits distribution  
- Correlation heatmaps  
- Segmentation analysis: campaign success across demographics  

### 4️⃣ A/B Testing
- Compare campaign performance (e.g., Campaign 1 vs Campaign 2)  
- Statistical significance testing using **Chi-square / t-test**  
- Visualize results in Tableau  

### 5️⃣ Predictive Modeling
- Build **Logistic Regression & Random Forest** models  
- Train/test split, cross-validation  
- Evaluate using Accuracy, F1 Score, AUC-ROC  
- Identify **key drivers of campaign success**  

### 6️⃣ Dashboard
- **Tableau / Google Data Studio** dashboard:  
  - Conversion Funnel  
  - Campaign Comparison  
  - Customer Segmentation  
  - ROI Tracker  

### 7️⃣ Insights & Recommendations
- Summarize findings in **Marketing_Report.pdf**  
- Provide actionable insights for budget allocation & customer targeting  

---

## 📈 Example Insights
- High-income customers have **3x higher conversion rates**.  
- Campaign 3 outperformed others with **statistical significance (p < 0.05)**.  
- Shifting 20% of budget towards Segment A increases ROI by **~15%**.  

---

## 🚀 How to Run the Project

### Clone the repo
```bash
git clone https://github.com/<your-username>/marketing-optimization-ds.git
cd marketing-optimization-ds
````

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run scripts

```bash
python src/data_preprocessing.py
python src/eda.py
python src/ab_testing.py
python src/modeling.py
```

---

## 📊 Dashboard

* Tableau/Google Data Studio Dashboard Link: [Coming Soon]
  (Save your dashboard link in `dashboards/dashboard_notes.txt`)

---

## 📑 Report

* Final Report: [`Marketing_Report.pdf`](reports/Marketing_Report.pdf)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

---

## 👨‍💻 Author

**Yash Pandey**

* Data Science Enthusiast | Problem Solver | Critical Thinker
* [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)

---

## ⭐ Acknowledgements

* Dataset from [Kaggle: Marketing Campaign Data](https://www.kaggle.com/datasets/jackdaoud/marketing-data)
* Inspired by real-world marketing analytics use cases

```