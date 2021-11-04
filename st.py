
import streamlit as st  # pip install streamlit
import openpyxl  
  
wb = openpyxl.load_workbook('project_data.xlsx')  
  
sheet = wb.active  
  
production = sheet['C3'].value  
disposal= sheet['C4'].value 



cell_range = ws['D8':'G3']

st.write(f'Backhoe production: {production} m3/hr')
st.write(f'Disposal distance: {disposal} knots')