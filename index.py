import pandas as pd
import streamlit as st
st.title(':green[AI Profit & Loss Statment]')
st.image("AI.png")
st.divider() 
st.markdown("This AI powered webapp will help you create profit and loss statment, Just follow the instruction given below...")
 
   

def consolidate_and_sum(df):
   import pandas as pd
import streamlit as st

# Function to consolidate descriptions, sum amounts, and find the most expensive amount
def consolidate_and_sum(df):
    consolidated_df = pd.DataFrame(columns=['Description', 'Total Amount', 'Most Expensive Amount'])

    for description in df['Description'].unique():
        try:
            total_amount = df.loc[df['Description'].str.contains(description), 'Amount'].sum()
            most_expensive_amount = df.loc[df['Description'].str.contains(description), 'Amount'].max()
        except Exception as e:
            st.warning(f"Error occurred while processing description: {description}. Error: {e}")
            continue

        consolidated_df = consolidated_df.append({'Description': description,
                                                  'Total Amount': total_amount,
                                                  'Most Expensive Amount': most_expensive_amount},
                                                 ignore_index=True)

    return consolidated_df

def main():
    st.title("Description Consolidation and Amount Summation")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.header("Original Data")
        st.write(df)

        # Perform consolidation, summing, and find most expensive amount
        try:
            consolidated_data = consolidate_and_sum(df)
            st.header("Consolidated Data")
            st.write(consolidated_data)
        except Exception as e:
            st.error(f"Error occurred during consolidation: {e}")

if __name__ == "__main__":
    main()

