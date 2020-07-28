import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime,date
import pyowm
from pyowm import OWM
from matplotlib import rcParams
from pytz import timezone
from pyowm.utils import timestamps

weather_api='0833f103dc7c2924da06db624f74565c'
owm=OWM(weather_api)


st.title("Weather Forecast")
st.write("## Made by Swarnabha with ❤️")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type :")
place=st.text_input("NAME OF THE CITY :", "")
unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))

g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))
b=st.button("SUBMIT")



def plot_line(days,min_t,max_t):        
        days=dates.date2num(days)
        rcParams['figure.figsize']=6,4
        plt.plot(days,max_t,color='green',linestyle='dashdot',linewidth = 1,marker='o',markerfacecolor='red',markersize=7) 
        plt.plot(days,min_t,color='orange',linestyle='dashdot',linewidth = 1,marker='o',markerfacecolor='blue',markersize=7)     
        plt.ylim(min(min_t)-4,max(max_t)+4)
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format=dates.DateFormatter('%m/%d')
        
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.grid(True,color='brown')
        plt.legend(["Maximum Temperaure","Minimum Temperature"],loc=1) 
        plt.xlabel('Dates(mm/dd)') 
        plt.ylabel('Temperature') 
        plt.title('5-Day Weather Forecast')   
        
        for i in range(5):
            plt.text(days[i], min_t[i]-1.5,min_t[i],
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        for i in range(5):
            plt.text(days[i], max_t[i]+0.5,max_t[i],
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        #plt.show()
        #plt.savefig('figure_line.png')
        st.pyplot()
        plt.clf()
        

def plot_bars(days,min_t,max_t):  
        #print(days)      
        rcParams['figure.figsize']=6,4
        days=dates.date2num(days)
        #print(days) 
        min_temp_bar=plt.bar(days-0.2, min_t, width=0.4, color='r')
        max_temp_bar=plt.bar(days+0.2, max_t, width=0.4, color='b')        
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format=dates.DateFormatter('%m/%d')
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.xlabel('Dates(mm/dd)') 
        plt.ylabel('Temperature') 
        plt.title('5-Day Weather Forecast')
        
        for bar_chart in [min_temp_bar,max_temp_bar]:
            for index,bar in enumerate(bar_chart):
                height=bar.get_height()
                xpos=bar.get_x()+bar.get_width()/2.0
                ypos=height 
                label_text=str(int(height))
                plt.text(xpos, ypos,label_text,
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        
        
        st.pyplot()
        plt.clf()
        
        

def find_min_max(place,unit,g_type):
    mgr=owm.weather_manager()
    days=[]
    dates_2=[]
    min_t=[]
    max_t=[]
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    if unit=='Celsius':
        unit_c='celsius'
    else:
        unit_c='fahrenheit'
    
    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date = day.date()
        if date not in dates_2:
            dates_2.append(date)
            min_t.append(None)
            max_t.append(None)
            days.append(date)
        temperature = weather.temperature(unit_c)['temp']
        if not min_t[-1] or temperature < min_t[-1]:
            min_t[-1]=temperature
        if not max_t[-1] or temperature > max_t[-1]:
            max_t[-1]=temperature
    #days = dates.date2num(days)
    #plt.xticks(days)
    #return days,min_t,max_t
    #print(f"| Minimum Temperature in {unit_c} for {place} is |",min_t)
    #print(f"| Maximum Temperature in {unit_c} for {place} is |",max_t)
    if g_type=="Line Graph":
        plot_line(days,min_t,max_t)
    elif g_type=="Bar Graph":
        plot_bars(days,min_t,max_t)
    i=0
    st.write(f"#    Date :  Max - Min  ({unit})")
    for obj in days:
        d=(obj.strftime("%d/%m"))
        st.write(f"### \v {d} :\t  ({max_t[i]} - {min_t[i]})")
        i+=1
      
    obs=mgr.weather_at_place(place)
    weather=obs.weather
    st.title(f"Details for {place} currently:")
    st.write(f"### Sky : {weather.detailed_status}")
    st.write(f"### Wind Speed : {weather.wind()['speed']} mph")
    st.write(f"### Sunrise Time : {weather.sunrise_time(timeformat='iso')} GMT")
    st.write(f"### Sunset Time : {weather.sunset_time(timeformat='iso')} GMT")
    
    
    st.title("Expected Temperature Changes/Alerts:")
    if forecaster.will_have_fog():
        st.write("### FOG ALERT!!")
    if forecaster.will_have_rain():
        st.write("### RAINY SCENES!!")
    if forecaster.will_have_storm():
        st.write("### STORM ALERT!!")
    if forecaster.will_have_snow():
        st.write("### SNOW ALERT!!")
    if forecaster.will_have_tornado():
        st.write("### TORNADO ALER!!")
    if forecaster.will_have_hurricane():
        st.write("### HURRICANE ALERT")
    if forecaster.will_have_clouds():
        st.write("### CLOUDY SKIES")    
    if forecaster.will_have_clear():
        st.write("### CLEAR WEATHER PREDICTED!!")
        
if b:
    if not place=="":    
        find_min_max(place,unit,g_type)
    
    
    
st.title("TOMORROW'S WEATHER FORECAST")
place1=st.text_input("NAME OF THE CITY FOR TOMORROW'S FORECAST:", "")
unit1=st.selectbox("Select Temperature Unit for tomorrow's forecast",("celsius","fahrenheit"))

hr1=st.slider("Hour :",min_value=0,max_value=23,step=1)
m1=st.slider("Minute :",min_value=0,max_value=59,step=5)
c=st.button("SUBMIT INFO ")    
    




def weather_detail(place,unit,hr,m):
    mgr=owm.weather_manager()
    forecaster = mgr.forecast_at_place(place, '3h')
    time=timestamps.tomorrow(hr,m)
    weather=forecaster.get_weather_at(time)
    
    t=weather.temperature(unit)['temp']
    st.write(f"## Temperature at {place} for the selected time in {unit} is {t}")
 
    st.title(f"Expected Temperature Changes/Alerts at {hr}:{m}")
    if forecaster.will_be_foggy_at(time):
        st.write("### FOG ALERT!!")
    if forecaster.will_be_rainy_at(time):
        st.write("### RAIN ALERT!!")
    if forecaster.will_be_stormy_at(time):
        st.write("### STORM ALERT!!")
    if forecaster.will_be_snowy_at(time):
        st.write("### SNOW ALERT!!")
    if forecaster.will_be_tornado_at(time):
        st.write("### TORNADO ALERT!!")
    if forecaster.will_be_hurricane_at(time):
        st.write("### HURRICANE ALERT")
    if forecaster.will_be_clear_at(time):
        st.write("### CLEAR WEATHER PREDICTED!!")
    if forecaster.will_be_cloudy_at(time):
        st.write("### CLOUDY SKIES")


if c:
    if not place:
        weather_detail(place1,unit1,hr1,m1)