import streamlit as st
from io import BytesIO
# from pyxlsb import open_workbook as open_xlsb
# import xlsxwriter
import pandas as pd
import openpyxl
import datetime

import warnings
warnings.simplefilter("ignore")

# This is the title to the code 
st.title('Combine Files')
st.write('This APP allows a user to Merge the Totara Module data with the WEP data, so that you have a combined view.')

# Uploads the file containing the TOTARA Data 
uploaded_file1 = st.file_uploader("Upload Totara Module data", key="1")
if uploaded_file1 is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file1.getvalue()
    # st.write(bytes_data)

    df1 = pd.read_excel(uploaded_file1)
    st.write(df1.head(3))

# Uploads the file containing the WEP data 
uploaded_file2 = st.file_uploader("Upload WEP data", key='2')
if uploaded_file2 is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file1.getvalue()
    # st.write(bytes_data)

    df2 = pd.read_excel(uploaded_file2)
    st.write(df2.head(3))
    
if st.button('Start Merge', key='3'):
    st.success('Merge Started')
    
    # Convert the column to uppercase
    df1['QID'] = df1['QID'].str.upper() # Totara data 
    st.write('DF1 - QID transformed to uppercase')
    st.write(df1.head(2))
    # Add a new column to df2 and fill it with an Excel formula
    df2.insert(loc=2, column='QID', value=None)
    st.write('DF2 - Column inserted')
    df2['QID'] = df2['Trainee'].str.extract(r'\((.*?)\)')
    # df2['QID'].apply(lambda x: '=DATEDIF("' + str(x) + '", TODAY(), "M")')
    # del df2['Trainee', 'Supervisors']
    st.write(df2.head(2))
    # df2['Months in DDP'] = df2[2].apply(lambda x: '=DATEDIF("' + str(x) + '", TODAY(), "M")')
    # # Convert the Excel formula strings to actual formulas
    # df2['Months in DDP'] = df2['Months in DDP'].apply(lambda x: None if x is None else x[1:] if x.startswith('=') else x)
    # df2['Months in DDP'] = pd.to_numeric(df2['Months in DDP'], errors='coerce')

    # # Convert the column to uppercase
    # df2['QID'] = df2['QID'].str.upper() 

    # Merge the dataframes based on the common column
    merged_df = pd.merge(df1, df2, on='QID')
    st.write(merged_df.head(5))
    # def writer():
    #     writer = pd.ExcelWriter('MergedReport.xlsx', engine='xlsxwriter')
    #     merged_df.to_excel(writer, sheet_name='Report')

    # def to_excel(merged_df):
    #     output = BytesIO()
    #     writer = pd.ExcelWriter(output, engine='xlsxwriter')
    #     merged_df.to_excel(writer, index=False, sheet_name='Report')
    #     workbook = writer.book
    #     worksheet = writer.sheets['Report']
    #     # format1 = workbook.add_format({'num_format': '0.00'}) 
    #     # worksheet.set_column('A:A', None, format1)  
    #     writer.save()
    #     processed_data = output.getvalue()
    #     return processed_data
    # df_xlsx = to_excel(merged_df)
    # st.download_button(label='📥 Download Current Result',
    #                             data=writer,
    #                             file_name= 'MergedReport.xlsx',
    #                             key='4')

    # merged_df.to_excel('NewReport.xlsx')
    # print(merged_df)

    st.success('All Merged')
    print('ALL DONE!')