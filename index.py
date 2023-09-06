import streamlit as st
import pandas as pd

import streamlit as stst
st.title(':green[AI Profit & Loss Statment]')
st.image("AI.png")
st.divider() 
st.markdown("This AI powered webapp will help you create profit and loss statment, Just follow the instruction given below...")
 


# Function to generate profit and loss sheet
def generate_profit_loss(df):
    # Convert column names to lowercase for consistency
    df.columns = df.columns.str.lower()
    
    # Filter positive and negative amounts
    income_df = df[df['amount'] > 0]
    expense_df = df[df['amount'] < 0]

    # Calculate total income and expenses
    total_income = income_df['amount'].sum()
    total_expense = expense_df['amount'].sum()

    # Calculate net profit (income - expenses)
    net_profit = total_income + total_expense

    return total_income, total_expense, net_profit

# Streamlit app
def main():
    st.title('Profit and Loss Statement')

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(uploaded_file)

            # Check if 'amount' and 'description' columns exist
            if 'amount' in df.columns and 'description' in df.columns:
                st.success("File successfully loaded!")
                st.write("Profit and Loss Statement:")

                total_income, total_expense, net_profit = generate_profit_loss(df)

                st.write(f"Total Income: ${total_income}")
                st.write(f"Total Expenses: ${total_expense}")
                st.write(f"Net Profit (Loss): ${net_profit}")

            else:
                st.error("The CSV file must have 'Amount' and 'Description' columns.")
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")

if __name__ == "__main__":
    main()
