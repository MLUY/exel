
import streamlit as st  # pip install streamlit
import openpyxl  
  
class Barge:
   def __init__(self,speed,hopper,hs_norm,color):
       self.speed=speed
       self.hopper=hopper
       self.hs_norm=hs_norm
       self.color=color 
  
  
wb = openpyxl.load_workbook('project_data.xlsx')  
  
sheet = wb.active  
  
production = sheet['C3'].value  
disposal= sheet['C4'].value 

cell_range = sheet['D8':'G10']

barges=[Barge(speed=cell_range[0][a].value,hopper=cell_range[1][a],hs_norm=cell_range[2][a],color=(colors[a],150)) for a in range(4)]

st.write(f'Backhoe production: {production} m3/hr')
st.write(f'Disposal distance: {disposal} knots')
st.write(f'1st Backhoe speed: {barges[0].speed} knots')
