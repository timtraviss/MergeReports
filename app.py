import streamlit as st
from io import BytesIO
import pandas as pd
import datetime
from datetime import date
import numpy as np

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
uploaded_file1 = st.file_uploader("Upload Totara Module data csv file", key="1")
if uploaded_file1 is not None:
  
    df1 = pd.read_csv(uploaded_file1)
    # Renames the Column User name to QID.
    df1.rename(columns= {'Username':'QID'}, inplace=True)
    # Turns the column into Uppercase
    df1['QID'] = df1['QID'].str.upper()
    # Writes out text on the webpage
    st.subheader('DF1 - Module Data')
    st.write(df1.head(3))

# Uploads the file containing the WEP data 
uploaded_file2 = st.file_uploader("Upload WEP data xlsx file", key='2')
if uploaded_file2 is not None:
 
    df2 = pd.read_excel(uploaded_file2)
    # Turns the QID Column to uppercase.
    df2.rename(columns= {'Trainee QID':'QID'}, inplace=True) 
    # Deletes the District Column from df2
    del df2['District']
    # Writes out text on the webpage
    st.subheader('DF2 - WEP Data')
    st.write(df2.head(3))

if st.button('Start Merge', key='3'):
    st.success('Merge Started')
    
    # Renames User's Fullname to Fullname
    df1.rename(columns= {'User\'s Fullname':'Fullname'}, inplace=True)
    # Renames the Column.
    df1.rename(columns= {'Progress (%)':'Modules (%)'}, inplace=True)
    # Renames the Column.
    df1.rename(columns= {'Due Date':'Months in DDP'}, inplace=True)

    # Strips QID of any spaces for both df1 and df2
    df1['QID'] = df1['QID'].str.strip()
    df2['QID'] = df2['QID'].str.strip()

    # Merge the dataframes based on the common column.
    merged_df = df1.merge(df2, on='QID', how='inner')
    print(merged_df)
   
    ### --- NEW CODE 
    # Turns the datetime into a datetime array.
    # Creates todays date.
    today = datetime.date.today()

    # Turns the DDC Completion Date Column into a date and displays it as a date. 
    merged_df['DDC Completion Date'] = pd.to_datetime(merged_df['DDC Completion Date'])
    # Turns the Months in DDP Column into a date and displays it as a date.
    merged_df['Months in DDP'] = pd.to_datetime(merged_df['Months in DDP'])
    today = pd.to_datetime(today)
    # Create the difference between the two dates.
    # today = datetime.date.today()
    date_delta = today - merged_df['DDC Completion Date']
    # Insert the date delta values into the 'Months in DDP' column
    # Calculate the date delta in days
    date_delta = (today - merged_df['DDC Completion Date']).dt.days
     # Convert days to months
    months_delta = (date_delta / 30.44).round(2)  # Assuming an average of 30.44 days in a month
    # Insert the months delta values into the 'Months in DDP' column
    merged_df['Months in DDP'] = months_delta
   
    # Change the date time format in these columns
    merged_df['Date Completed'] = pd.to_datetime(merged_df['Date Completed'])
    merged_df['Date Completed'] = merged_df['Date Completed'].dt.strftime('%d %b %Y')
    # Change the date time format in these columns
    merged_df['WEP Start Date'] = pd.to_datetime(merged_df['WEP Start Date'])
    merged_df['WEP Start Date'] = merged_df['WEP Start Date'].dt.strftime('%d %b %Y')
    # Change the date time format in these columns
    merged_df['DQC Completion Date'] = pd.to_datetime(merged_df['DQC Completion Date'])
    merged_df['DQC Completion Date'] = merged_df['DQC Completion Date'].dt.strftime('%d %b %Y')
    # Filters on the blank values in this dataframe
    # merged_df['DQC Completion Date'] = merged_df[merged_df['DQC Completion Date'].str.len() > 0]
    merged_df['DDC Completion Date'] = pd.to_datetime(merged_df['DDC Completion Date'])
    merged_df['DDC Completion Date'] = merged_df['DDC Completion Date'].dt.strftime('%d %b %Y')
    # Filters on the blank values in this dataframe
    merged_df['WEP Completed Date'] = pd.to_datetime(merged_df['WEP Completed Date'])
    merged_df['WEP Completed Date'] = merged_df['WEP Completed Date'].dt.strftime('%d %b %Y')
   
    # Delete the columns that are not required.
    del merged_df['Job Location']
    del merged_df['Program Short Name']
    del merged_df['Programme Suspended']
    del merged_df['Date Suspended']
    del merged_df['Leave Type']
    del merged_df['Leave Return']
    del merged_df['INV Other']
    del merged_df['Wing number']
    # del merged_df['Trainee']
    del merged_df['WEP Completed By']
    #This is wanted by Nicole - del merged_df['WEP Completed Date']
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

    # Rename the columns. 
    merged_df.rename(columns= {'WEP Completion Percentage':'WEP (%)'}, inplace=True)
    ## Print Statements
  
    @st.cache_data
    #Function to merge and encode data from dataframe to csv file. 
    def convert_df(merged_df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return merged_df.to_csv(index=False).encode('utf-8')

    csv = convert_df(merged_df)
    st.success('Download Ready')
    
    # Download Button. 
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='NewMergedReport.csv',
        mime='text/csv'
        )
    
    

    
