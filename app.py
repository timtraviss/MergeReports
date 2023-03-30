import streamlit as st
import os
import pandas as pd
from io import StringIO
# import warnings
# warnings.simplefilter("ignore")

# This is the title to the code 
st.title('Combine Files')

#Uploads the file
import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)

#     folder = r'/Users/timothytraviss/Desktop/WEP_Excel_Files/'
#     df_total = pd.DataFrame()

#     files = os.listdir(folder)
#     files
#     for file in files: #loop through excel files
#         if file.endswith('.xlsx'):
#             excel_file = pd.ExcelFile(f'{folder}/{file}')
#             sheets = excel_file.sheet_names
#             for shhet in sheets: #loop through the sheets
#                 df = excel_file.parse()
#                 df_total = df_total.append(df)
    #This prints out a message in the console to sya that it worked. 

    # OLD CODE 
    # df_total.to_excel(f'{folder}/combinedfile.xlsx')
    # print('\n')
    # print('This has worked and your file is now ready')
    # st.success('This has worked and your file is now ready')
    # print('\n')