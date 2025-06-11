import streamlit as st
import pandas as pd

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("💰 پاکستان انکم ٹیکس کیلکولیٹر (2025-26)")
st.markdown("یہ ایپلیکیشن آپ کی ماہانہ تنخواہ کی بنیاد پر سال 2025-26 کے مطابق انکم ٹیکس کا حساب لگاتی ہے۔")

# User input
monthly_salary = st.number_input("📥 اپنی ماہانہ تنخواہ درج کریں (روپے میں)", min_value=0, step=1000)

# Compute annual salary
annual_salary = monthly_salary * 12

# Tax slabs definition
tax_slabs = [
    {"min": 0,         "max": 600000,    "fixed": 0,       "rate": 0},
    {"min": 600001,    "max": 1200000,   "fixed": 0,       "rate": 0.01},
    {"min": 1200001,   "max": 2200000,   "fixed": 6000,    "rate": 0.11},
    {"min": 2200001,   "max": 3200000,   "fixed": 116000,  "rate": 0.23},
    {"min": 3200001,   "max": 4100000,   "fixed": 346000,  "rate": 0.30},
    {"min": 4100001,   "max": float("inf"), "fixed": 616000,  "rate": 0.35},
]

def calculate_tax(income):
    for slab in tax_slabs:
        if slab["min"] <= income <= slab["max"]:
            extra_income = income - slab["min"]
            tax = slab["fixed"] + extra_income * slab["rate"]
            return round(tax, 2), slab
    return 0, None

# Calculate tax
annual_tax, slab_info = calculate_tax(annual_salary)
monthly_tax = round(annual_tax / 12, 2) if annual_tax else 0

# Show result
st.subheader("📊 نتیجہ:")
st.write(f"**سالانہ آمدن:** {annual_salary:,.0f} روپے")
st.write(f"**سالانہ انکم ٹیکس:** {annual_tax:,.0f} روپے")
st.write(f"**ماہانہ انکم ٹیکس:** {monthly_tax:,.0f} روپے")

if slab_info:
    st.markdown("**آپ اس سلیب میں آتے ہیں:**")
    st.write(f"- فکسڈ ٹیکس: {slab_info['fixed']:,.0f} روپے")
    st.write(f"- اضافی آمدن پر ٹیکس ریٹ: {int(slab_info['rate']*100)}٪")

# Show tax slab table
st.subheader("📚 انکم ٹیکس سلیبز (2025-26)")

slab_df = pd.DataFrame([
    ["0 - 6 لاکھ", "0", "0٪"],
    ["6 - 12 لاکھ", "0", "1٪"],
    ["12 - 22 لاکھ", "6,000", "11٪"],
    ["22 - 32 لاکھ", "116,000", "23٪"],
    ["32 - 41 لاکھ", "346,000", "30٪"],
    ["41 لاکھ سے زائد", "616,000", "35٪"],
], columns=["سالانہ آمدن", "فکسڈ ٹیکس", "اضافی آمدن پر ٹیکس ریٹ"])

st.table(slab_df)
