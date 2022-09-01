import streamlit as st
import pandas as pd
import calendar

# initialize calendar
cal = calendar.TextCalendar()

# page setup
page_title = 'Calendar'
page_icon = '📅'
st.set_page_config(page_title=page_title, page_icon=page_icon)

st.title('Calendar')
date = st.date_input('Select date: Year / Month / Day', value=pd.to_datetime("today", format="%Y-%m-%d"))

st.write('Calendar month: %s'%date.month)
st.write('Calendar year: %s'%date.year)

    
