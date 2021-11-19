
import streamlit as st  # pip install streamlit
import pandas as pd
import openpyxl  
  
class Barge:
   def __init__(self,speed,hopper,hs_norm,color):
       self.speed=speed
       self.hopper=hopper
       self.hs_norm=hs_norm
       self.color=color 
 
colors=['olive','navy','red','blue']
  
wb = openpyxl.load_workbook('project_data.xlsx')  
  
sheet = wb.active  
  
production = sheet['C3'].value  
disposal= sheet['C4'].value 

cell_range = sheet['D8':'G10']

barges=[Barge(speed=cell_range[0][a].value,hopper=cell_range[1][a],hs_norm=cell_range[2][a],color=(colors[a],150)) for a in range(4)]

st.write(f'Backhoe production: {production} m3/hr')
st.write(f'Disposal distance: {disposal} knots')

st.write(f'1st Backhoe speed: {barges[0].speed} knots')
st.write(f'2nd Backhoe speed: {barges[1].speed} knots')
st.write(f'3rd Backhoe speed: {barges[2].speed} knots')
st.write(f'4th Backhoe speed: {barges[3].speed} knots')

# ---- READ EXCEL ----
@st.cache
def read_file():
    df = pd.read_excel(
        io=uploaded_file,
        engine="openpyxl",
        sheet_name="data",
        skiprows=3,
        usecols="A:V",
        nrows=8000,
    )
    
    return df

#radio buttons
status=st.radio('how do you want to feed in data',('upload excel','manual entry'))

if status=='upload excel':
    uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")        

else:
    st.write('pfff')   

if uploaded_file:
    df=read_file()
    #df['date']=df.apply(lambda x: datetime.date(df['YYYY'], df['MM'], df['DD'],df['HH']),axis=1)
    st.dataframe(df)










