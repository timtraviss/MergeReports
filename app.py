import streamlit as st
from io import BytesIO
# from pyxlsb import open_workbook as open_xlsb
# import xlsxwriter
import pandas as pd
import openpyxl
import datetime

import warnings
warnings.simplefilter("ignore")


st.set_page_config(layout="wide", 
                   page_icon=":clipboard:", 
                   page_title="Merge Reports"
                   )


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
    
    # Convert the column to uppercase, df1 equals the totara data. 
    df1['QID'] = df1['QID'].str.upper() 
    df1.rename(columns= {'Progress (%)':'Modules (%)'}, inplace=True)
    st.write('DF1 - QID transformed to uppercase')

    st.write(df1.head(2))
    # Add a new column to df2 and fill it with an Excel formula.
    df2.insert(loc=2, column='QID', value=None)
    # Extract the QID from the Trainee Column. 
    df2['QID'] = df2['Trainee'].str.extract(r'\((.*?)\)')
    del df2['District']
    del df2['Supervisors']
    # Merge the dataframes based on the common column.
    merged_df = pd.merge(df1, df2, on='QID')
   
    # Change the date time format in these columns
    merged_df['Date Completed'] = pd.to_datetime(merged_df['Date Completed'])
    merged_df['Date Completed'] = merged_df['Date Completed'].dt.strftime('%d %b %Y')

    merged_df['DDC Completion Date'] = pd.to_datetime(merged_df['DDC Completion Date'])
    merged_df['DDC Completion Date'] = merged_df['DDC Completion Date'].dt.strftime('%d %b %Y')

    merged_df['WEP Start Date'] = pd.to_datetime(merged_df['WEP Start Date'])
    merged_df['WEP Start Date'] = merged_df['WEP Start Date'].dt.strftime('%d %b %Y')

    merged_df['DQC Completion Date'] = pd.to_datetime(merged_df['DQC Completion Date'])
    merged_df['DQC Completion Date'] = merged_df['DQC Completion Date'].dt.strftime('%d %b %Y')
    
    # Delete the columns that are not required.
    del merged_df['Job Location']
    del merged_df['Program Short Name']
    del merged_df['Programme Suspended']
    del merged_df['Date Suspended']
    del merged_df['Leave Type']
    del merged_df['Leave Return']
    del merged_df['INV Other']
    del merged_df['Wing number']
    del merged_df['Trainee']
    del merged_df['WEP Completed By']
    del merged_df['WEP Completed Date']
    del merged_df['WEP Moderation Details']
    ## Columns required in Merged Report 
    # QID
    # Fullname
    # District 
    # Program Status 
    # Due Date
    # Modules (%)
    # Date Completed 
    # Course Name
    # Course Status 
    # Final Grade
    # DDC Completion Date 
    # Months in DDP
    # DDC Completion Date 
    # Months in DDP
    # DQC Completion Date 
    # WEP Start Date 
    # WEP (%)
    # WEP Status
    # WEP Completed Date

 
    # Rename the columns 
    merged_df.rename(columns= {'WEP Completion Percentage':'WEP (%)'}, inplace=True)
    ## Print Statements
    print('renamed')
    st.write('Merged_df')
    st.write(merged_df.head(5))

    @st.cache_data
    def convert_df(merged_df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return merged_df.to_csv().encode('utf-8')

    csv = convert_df(merged_df)

    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='MergedReport.csv',
    mime='text/csv',
)

    # writer = pd.ExcelWriter('MergedReport.xlsx', engine='xlsxwriter')
    # writer.save(filename='MergedReport.xlsx')
    # # writer.save()
    # merged_df.to_excel(writer, sheet_name='Report')
    # st.success('All Merged')
    # st.download_button(label='📥 Download Current Result',
    #                         data=BytesIO(writer.getvalue()),
    #                         file_name= 'MergedReport.xlsx',
    #                         key='4')    
    print('ALL DONE!')

    # st.download_button(label='📥 Download Current Result',
    #                data=writer,
    #                file_name='MergedReport.xlsx',
    #                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    #                on_click=':download')

    
    # print('ALL DONE!')