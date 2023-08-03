import pandas as pd
import streamlit as st
st.title(':green[AI Profit & Loss Statment]')
st.image("AI.png")
st.divider() 
st.markdown("This AI powered webapp will help you create profit and loss statment, Just follow the instruction given below...")
 
   

def consolidate_and_sum(df):
    consolidated_df = pd.DataFrame(columns=['Description', 'Amount'])

    for description in df['Description'].unique():
        total_amount = df.loc[df['Description'].str.contains(description), 'Amount'].sum()
        consolidated_df = consolidated_df.append({'Description': description, 'Amount': total_amount}, ignore_index=True)

    return consolidated_df

def main():
    st.write("Step & Instructions")

    bullet_points = [
        "Step1 Profit & Loss Statement Cleansing",
        "Step2 Coming soon",
        "Step3 Coming soon",
        "Step4 Coming soon",
        "Step5Coming soon"
    ]

    st.header("Follow the steps")
    st.write(bullet_points, type="unordered")

    st.subheader("**Step 1** _Profit & Loss Statement Cleansing_")
    st.write("_Download your business bank account statement in **csv** and upload it here, make sure you have descirption and amount column in your **csv** file_")
    st.write("this step will cleanse your file and consolidate duplicate and sum amount")

    # File upload
    uploaded_file = st.file_uploader("Now upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        #st.header("Original Data")
        #st.write(df)
        # Perform consolidation and summing
        consolidated_data = consolidate_and_sum(df)

        st.header("Consolidated Data of Description")
        st.write("Added similar items with amount sum")
        st.write(consolidated_data)

        
    st.divider() 
    st.write(":Blue[By Syed Abbas]")
    st.write("Let me know what else do you want I can add here")
    st.markdown("My Medium Page: [https://https://medium.com/@SyedAbbasT](https://https://medium.com/@SyedAbbasT)")

if __name__ == "__main__":
    main()
