import streamlit as st
import numpy as np
import pandas as pd

st.title("Employee Attrition Dashboard", icon=":material/dashboard:")
st.markdown("""

Why do employees leave? This dashboard looks at 1,470 employees from IBM's HR Analytics dataset and shows who left and in which groups.

Use the filters on the left to narrow things down. **Attrition rate** means the percent of employees in a group who left. This is a practice dataset, not real company data.


""")

data = pd.read_csv('data/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Turn Attrition into 0 and 1 (Label Encoding)

data['Attrition'] = data['Attrition'].map({'Yes': 1, 'No': 0})
st.write(data.head())

col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", data.shape[0], border=True, icon="💼")

total = data['Attrition'].sum() # Number of employees who left

avg = (total / data.shape[0])
col2.metric("Number who left", total, border=True, icon="✂️")
col3.metric("Attrition Rate", f"{avg:.2%}" , border=True, icon="📊")


# Using "with" notation
with st.sidebar:
    choice = st.pills(
        "View Attrition rate by ",
        ["Department", "Overtime", "Age"],
        default='Department'
    )   

if choice is None:
    choice = "Department"

# If choice is Department
if choice == "Department":
    st.bar_chart(data['Department'])