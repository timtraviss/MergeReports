import streamlit as st
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import xlsxwriter
import pandas as pd
import openpyxl

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
    st.write(df1.head(3))
    
if st.button('Start Merge', key='3'):
    st.success('Merge Started')
    
    # Convert the column to uppercase
    df1['QID'] = df1['QID'].str.upper() # Totara data 
    

    # Insert formula into WEP data df2 
    # https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
    df2.insert(3, "QID", [f'=MID(A2,FIND("(",A2)+1,FIND(")",A2)-FIND("(",A2)-1)'], True) #do I need to filldown?
    df2['QID'] = df2['QID'].str.upper() # WEP data 
    # del df['column_name']
    del df2[1,3]

    # Merge the dataframes based on the common column
    merged_df = pd.merge(df1, df2, on='QID')
    merged_df.insert(11, 'Months in DDP', [f'=sum(today()-k2/30.41)']) # do I need to filldown?

    def writer():
        writer = pd.ExcelWriter('MergedReport.xlsx', engine='xlsxwriter')
        merged_df.to_excel(writer, sheet_name='Report')

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
    st.download_button(label='📥 Download Current Result',
                                data=writer,
                                file_name= 'MergedReport.xlsx',
                                key='4')

    # merged_df.to_excel('NewReport.xlsx')
    # print(merged_df)

    st.success('All Merged')
    print('ALL DONE!')