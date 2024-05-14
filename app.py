import streamlit as st
from io import BytesIO
import pandas as pd
import datetime
from datetime import date
import numpy as np
import xlsxwriter
import openpyxl

import warnings
warnings.simplefilter("ignore")

st.set_page_config(layout="wide", 
                   page_icon=":clipboard:", 
                   page_title="Modules Report"
                   )

# This is the title to the code 
st.title('Modules Report')
st.write('This report details the number of modules that were sat in a given month.')
st.write('It also has a dashboard that gives you a count as to the number of modules sat and the average score for the modules sat.')
st.warning('It does not record fails.')

# NEW CODE
# This is the uploader for the excel file. 
uploaded_file1 = st.file_uploader("Upload Modules Report", key='1')

if uploaded_file1 is not None:
    df1 = pd.read_excel(uploaded_file1)
    if st.button('Create Dashboard', key='2'):
        st.success('Dashboard Completed')

        # You need to either provide the path to an existing Excel file
        # or create a new Excel file before attempting to open it
        workbook = openpyxl.Workbook()

        # Create a new worksheet named 'dashboard'
        dashboard_sheet = workbook.create_sheet('Dashboard')

        # Count the number of modules in column A of the first worksheet
        module_count = df1['A'].count()

        # Calculate the average score in column B of the first worksheet
        average_score = df1['B'].mean()

        # Write the module count and average score to the 'Dashboard' worksheet
        dashboard_sheet['A1'] = 'Module Count'
        dashboard_sheet['B1'] = module_count
        dashboard_sheet['A2'] = 'Average Score'
        dashboard_sheet['B2'] = average_score

        # Save the modified workbook
        workbook.save('Monthly_Modules_Report.xlsx')

        st.download_button(
            label="Download data as XLSX",
            data=open('Monthly_Modules_Report.xlsx', 'rb'),
            file_name='Monthly_Modules_Report.xlsx'
        )





    
    


    


    
