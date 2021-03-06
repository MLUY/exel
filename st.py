import streamlit as st  # pip install streamlit
import pandas as pd
import datetime as dt
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
  
# ----- werkbaarheid.xlsx - standard format Hydronamic
    all_column_names= ['year',
                       'month',
                       'day',
                       'hour',
                       'u10',
                       'u10d',
                       'tide',
                       'Hm0',
                       'Theta',
                       'Tp',                   
                       'Tz',
                       'Tm',
                       'Hm0_Sea',
                       'Theta_Sea',
                       'Tp_Sea',
                       'Tz_Sea',
                       'Tm_Sea',
                       'Hm0_Swell',
                       'Theta_Swell',
                       'Tp_Swell',                  
                       'Tz_Swell',
                       'Tm_Swell'] 
  
    cols=[0, 1, 2, 3, 6, 7, 9, 10]   
        
    df=pd.read_excel(io=uploaded_file,engine="openpyxl",sheet_name="data",skiprows=3,usecols=cols)
        
    df.columns=['year', 'month', 'day', 'hour','tide','Hm0','Tp','Tz']    
    
    
    # ,skiprows=3,usecols=[0,1,2,3,7],names=['year', 'month', 'day', 'hour','Hm0'],nrows=8767
    # ,nrows=8767
    
    df["date_time"]=pd.to_datetime(df[["year", "month", "day", "hour"]])
    df.sort_values(by="date_time",inplace=True)
    df["delta"] = df["date_time"].diff(1).astype("timedelta64[h]")
    
    return df

#radio buttons
status=st.radio('how do you want to feed in data',('upload excel','manual entry'))

if status=='upload excel':
    uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")        
    df=read_file()
    st.dataframe(df)
   
    
    
else:
    st.write('pfff')   



with st.echo(code_location='below'):
    import matplotlib.pyplot as plt
    
    Hs=df['Hm0']
    Tp=df['Tp']
    Tz=df['Tz']
    tm=df['tide']
    dm=df['date_time']    

    fig,ax=plt.subplots(1,4,figsize=(18,5))

    ax[0].hist(Hs,color='#de3517',bins=15,edgecolor='k',density=True)
    ax[0].set_xlim(0,5)
    #ax[0].set_xlabel('histogram')

    ax[1].scatter(Tp,Hs,color='green',s=1,label='thats nice')
    ax[1].scatter(Tz,Hs,color='blue',s=1,label='thats not nice')
    ax[1].legend()
    ax[1].set_xlabel('oops', fontsize=14)
    ax[1].grid()

    ax[2].scatter(Tz,Hs,s=1)

    ax[3].plot(dm,tm,color='#f0d20f',label='thats nice',linewidth=0.5)
    
    st.write(fig)



