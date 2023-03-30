import streamlit as st
import os
import pandas as pd
from io import StringIO
# import warnings
# warnings.simplefilter("ignore")

# This is the title to the code 
st.title('Combine Files')

# Uploads the file


uploaded_file1 = st.file_uploader("Choose a file", key="1")
if uploaded_file1 is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file1.getvalue()
    # st.write(bytes_data)

    df1 = pd.read_excel(uploaded_file1)
    st.write(df1.head(3))

uploaded_file2 = st.file_uploader("Choose a file", key='2')
if uploaded_file2 is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file1.getvalue()
    # st.write(bytes_data)

    df2 = pd.read_excel(uploaded_file2)
    st.write(df1.head(3))
    
    # Convert the column to uppercase
    df1['QID'] = df1['QID'].str.upper()
    df2['QID'] = df2['QID'].str.upper()

    print(df1, df2)

    # Merge the dataframes based on the common column
    merged_df = pd.merge(df1, df2, on='QID')

    merged_df.to_excel('/Users/timothytraviss/Desktop/LearningToCode/MergeReports/NewReport.xlsx')
    print(merged_df)

    print('ALL DONE!')