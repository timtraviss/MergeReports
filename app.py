import streamlit as st
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
#import os
import pandas as pd
#from io import StringIO
# import warnings
# warnings.simplefilter("ignore")

# This is the title to the code 
st.title('Combine Files')
st.write('This APP allows a user to Merge the Totara Module data with the WEP data, so that you have a combined view.')
# Uploads the file
#test

uploaded_file1 = st.file_uploader("Upload Totara Module data", key="1")
if uploaded_file1 is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file1.getvalue()
    # st.write(bytes_data)

    df1 = pd.read_excel(uploaded_file1)
    st.write(df1.head(3))

uploaded_file2 = st.file_uploader("Upload WEP data", key='2')
if uploaded_file2 is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file1.getvalue()
    # st.write(bytes_data)

    df2 = pd.read_excel(uploaded_file2)
    st.write(df1.head(3))
    
if st.button('Start Merge'):
    st.success('Merge Started')
    # Convert the column to uppercase
    df1['QID'] = df1['QID'].str.upper()
    df2['QID'] = df2['QID'].str.upper()

    # Merge the dataframes based on the common column
    merged_df = pd.merge(df1, df2, on='QID')

    def to_excel(merged_df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        merged_df.to_excel(writer, index=False, sheet_name='Report')
        workbook = writer.book
        worksheet = writer.sheets['Report']
        # format1 = workbook.add_format({'num_format': '0.00'}) 
        # worksheet.set_column('A:A', None, format1)  
        writer.save()
        processed_data = output.getvalue()
        return processed_data
    df_xlsx = to_excel(merged_df)
    st.download_button(label='📥 Download Current Result',
                                data=df_xlsx ,
                                file_name= 'MergedReport.xlsx')

    # merged_df.to_excel('NewReport.xlsx')
    # print(merged_df)

    # with open(file_name, "rb") as template_file:
    #     template_byte = template_file.read()

    # st.download_button(label="Click to Download Template File",
    #                     data=template_byte,
    #                     file_name="template.xlsx",
    #                     mime='application/octet-stream')
    st.success('All Merged')
    print('ALL DONE!')