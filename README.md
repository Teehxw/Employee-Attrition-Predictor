# Employee Attrition Predictor

Predicts which employees are likely to leave a company using machine learning, trained on IBM's HR Analytics dataset.

I looked at what the data says about why people leave, then built two models to predict who is at risk and compared them.

---

## Results at a glance

- **Dataset:** 1,470 employees, 35 columns. Only 16% of employees (237) left.
- **Final model:** Logistic regression.
- **It caught 66% of the employees who left**, with 75% overall accuracy.
- **A random forest scored higher on accuracy (83%) but caught only 30% of the people who left**, so I did not pick it.

---

## What I found in the data

These patterns come from the charts in the notebook:

- **Pay:** Employees who left had a noticeably lower median monthly income.
- **Age:** Leavers were mostly in their 20s and 30s. People over 40 rarely left.
- **Overtime:** Employees working overtime left much more often than those who didn't.
- **Job role:** Sales Representatives and Laboratory Technicians had the worst retention. Managers and Research Directors almost never left.
- **Department:** Sales had the highest share of people leaving.
- **Travel:** Employees who travel frequently left more often than those who don't travel.

Overall, pay, workload, and travel stand out, which points to work-life balance as a big part of the story. These are links in the data, not proof of what causes people to leave.

![Top 10 factors](images/feature_importance.png)

The chart above shows the factors the random forest relied on most: MonthlyIncome, Age, TotalWorkingYears, DailyRate, and YearsAtCompany led the list, and OverTime was also in the top 10. It shows which columns matter, not which direction they push. DailyRate, MonthlyRate, and HourlyRate are probably noise in this dataset, so I would treat them with caution.

---

## How I built it

1. **Explored the data.** Checked the size, column types, and missing values (there were none). Made charts of attrition by department, age, income, overtime, job role, and travel.
2. **Cleaned it.** Dropped columns that can't help a model: `EmployeeCount`, `StandardHours`, and `Over18` (the same value in every row) and `EmployeeNumber` (just an ID).
3. **Turned text into numbers.** `Attrition` became 1 (left) or 0 (stayed). The other text columns, like department and job role, became 0/1 columns using one-hot encoding.
4. **Split the data 80/20.** The model learned from 80% and was tested on 20% it had never seen. The split keeps the same share of leavers in both parts.
5. **Trained two models.** Logistic regression (with scaled data) and a random forest with 200 trees. Both were told to pay extra attention to the smaller group of employees who left.
6. **Compared them and saved the winner.**

---

## Model comparison

The test set had 294 employees: 247 stayed and 47 left.

| | Logistic Regression | Random Forest |
|---|---|---|
| Overall accuracy | 75% | 83% |
| Employees who left that it caught (recall) | **66%** | 30% |
| Right when it said "will leave" (precision) | 35% | 44% |

**Why I didn't pick the model with higher accuracy:** Because 84% of employees stayed, a model that guessed "stayed" for everyone would be about 84% accurate and catch nobody. The random forest's accuracy mostly comes from being right about people who stay. Logistic regression caught more than twice as many of the people who actually left, which is the point of the project.

---

## One mistake I fixed

My first feature importance chart showed `EmployeeNumber` in the top 10. That column is only an ID, so it can't really explain why someone leaves. It meant the models were learning from noise. I removed it and reran everything, and the results here are from the clean run.

---

## Limits

- **It's a screening tool, not a final answer.** When the model flags someone, it's right only about 1 time in 3.
- **Links, not causes.** Overtime goes with leaving, but this project can't show that overtime makes people leave.
- **Small test set.** 47 employees who left is a small group, so the numbers could shift on different data.
- **Sample dataset.** This is a well-known practice dataset, not a real company's records.

## What I'd do next

- Try adjusting how confident the model needs to be before it flags someone, to trade off catching more leavers against false alarms.
- Test other models and use cross-validation for steadier numbers.
- Build a simple dashboard so an HR team could explore the patterns without reading a notebook.

---

## Tech stack

Python, pandas, NumPy, matplotlib, seaborn, scikit-learn, joblib, Jupyter Notebook

---

## Run it yourself

### 1. Clone the repo

```bash
git clone https://github.com/Teehxw/employee-attrition.git
cd employee-attrition
```

### 2. Install the libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
```

### 3. Get the data

Download **IBM HR Analytics Employee Attrition & Performance** from Kaggle and put the CSV in the `data` folder:

```
data/WA_Fn-UseC_-HR-Employee-Attrition.csv
```

### 4. Open the notebook

```bash
jupyter notebook notebook.ipynb
```

Run the cells from top to bottom.

### Use the saved model

```python
import joblib

model = joblib.load('model/attrition_model.joblib')
scaler = joblib.load('model/scaler.joblib')

# new_data must have the same columns as the training data
prediction = model.predict(scaler.transform(new_data))
```

---

## Project structure

```
employee-attrition/
├── notebook.ipynb      # data exploration, cleaning, and models
├── data/               # dataset goes here (not included)
├── model/
│   ├── attrition_model.joblib
│   └── scaler.joblib
├── images/
│   └── feature_importance.png
└── README.md
```

---

## Author

Built by [@Teehxw](https://github.com/Teehxw)
