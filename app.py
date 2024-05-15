import streamlit as st
from io import BytesIO
import pandas as pd
import datetime
from datetime import date
import numpy as np
import xlsxwriter

import warnings
warnings.simplefilter("ignore")

import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

# ... (the rest of your code remains the same) ...

if st.button('Create Dashboard', key='2'):
    st.success('Dashboard Completed')
    workbook = openpyxl.Workbook()

    # Create a new worksheet for the original data
    original_data_sheet = workbook.active
    original_data_sheet.title = 'Original Data'

    # Write the dataframe to the 'Original Data' worksheet
    for row in dataframe_to_rows(df1, index=False, header=True):
        original_data_sheet.append(row)

    # Create a new worksheet named 'Dashboard'
    dashboard_sheet = workbook.create_sheet('Dashboard')

    # Count the number of modules in column A of the 'Original Data' worksheet
    module_count = df1['User ID'].count()

    # Calculate the average score in column B of the 'Original Data' worksheet
    average_score = df1['Grade'].mean()

    # Write the module count and average score to the 'Dashboard' worksheet
    dashboard_sheet['A1'] = 'Module Count'
    dashboard_sheet['A2'] = module_count
    dashboard_sheet['B1'] = 'Average Score'
    dashboard_sheet['B2'] = average_score

    # Save the modified workbook
    workbook.save('Monthly_Modules_Report.xlsx')

    st.download_button(
        label="Download data as XLSX",
        data=open('Monthly_Modules_Report.xlsx', 'rb'),
        file_name='Monthly_Modules_Report.xlsx'
    )
    
    


    


    
