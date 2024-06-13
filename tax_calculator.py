import streamlit as st
import pandas as pd

def calculate_tax(income):
    if income <= 600000:
        return 0
    elif income <= 1200000:
        return (income - 600000) * 0.15
    elif income <= 1600000:
        return 90000 + (income - 1200000) * 0.20
    elif income <= 3600000:
        return 170000 + (income - 1600000) * 0.30
    elif income <= 5600000:
        return 650000 + (income - 3600000) * 0.40
    else:
        return 1610000 + (income - 5600000) * 0.45

def main():
    st.title("Income Tax Calculator (FY 2024-25)")

    # Option to select income type (yearly or monthly)
    income_type = st.radio("Select your income type:", ('Yearly', 'Monthly'))

    # Input field for the user to enter their income
    income = st.number_input("Enter your income in Rs", min_value=0, value=0, step=1000)

    if income_type == 'Monthly':
        income *= 12

    # Calculate the tax based on the income
    tax = calculate_tax(income)

    # Display the calculated tax
    st.write(f"The calculated tax on an {income_type.lower()} income of Rs {income} is Rs {tax:.2f}")

    # Calculate the remaining income after tax
    remaining_income = income - tax

    # Create a DataFrame for the bar chart
    data = pd.DataFrame({
        'Amount': [tax, remaining_income],
        'Category': ['Tax', 'Remaining Income']
    })

    # Display the bar chart
    st.bar_chart(data.set_index('Category'))

if __name__ == "__main__":
    main()
