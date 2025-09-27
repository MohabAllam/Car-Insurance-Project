
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout= 'wide', page_title= 'Car Insurance Project')

html_title = "<h1 style=color:white;text-align:center;> Car Insurance Classification Project </h1>"
st.markdown(html_title, unsafe_allow_html=True)

st.image('https://prod.cosy.bmw.cloud/bmwweb/cosySec?COSY-EU-100-2545xM4RIyFnbm9Mb3AgyyIJrjG0suyJRBODlsrjGpuaprQbhSIqppglBgMxEJl384MlficYiGHqoQxYLW7%25f3tiJ0PCJirQbLDWcQW7%251uNRrqoQh47wMvcYi9t5BJMb3islBglUUJecRScH8R4MbnMdoPeyJGy53LvrQ%25r9YaJW8zWuEJQqogqaFQ7l3ilUjzJcRScH78lMbnMd0zqyJGy5iubrQ%25r9SbUW8zWunDjqogqaG4zl3ilU%25QocRScHzUVMbnMdg4ayJGy5iJUrQ%25r9saYW8zWuKbGqogqaDJKl3ilUCQIcRScH4%25bMbnMdJmSyJGy5Q3SrQ%25r98R5W8zWuobuqogqa3Jnl3ilUR%25gcRScHbU8MbnMdJbkyJGy5Q4ErQ%25r993UW8zWuu3HqogqaaUbl3ilUjv0cRSrQdr9SMBW8zcRacHHwsMbnW85WuEfuqoQEdcNq0zxcqW8JuzM8nq0z6Fboy6oEd82')

df = pd.read_csv('cleaned_df.csv')
st.dataframe(df)

kidsdriv = st.selectbox('PLease provid number of driving kids', df.kidsdriv.unique())
age = st.sidebar.slider('Enter your Age', min_value= 16, max_value= 81, step= 1)
homekids = st.selectbox('PLease provid total number of kids', df.homekids.unique())
yoj = st.sidebar.slider('Please provide number of years on job', min_value= int(df.yoj.min()), max_value= int(df.yoj.max()), step= 1)
income = st.number_input('Please provide your income', min_value= df.income.min(), max_value= df.income.max())
parent1 = st.selectbox('PLease select whether you are single parent or not', df.parent1.unique())
home_val = st.number_input('Please provide your home value', min_value= df.home_val.min(), max_value= df.home_val.max())
mstatus = st.sidebar.radio('Marital Status', df.mstatus.unique())
gender = st.sidebar.radio('Gender', df.gender.unique())
education = st.selectbox('Please enter your educational background', df.education.unique())
occupation = st.selectbox('Please enter your Occupation', df.occupation.unique())
travtime = st.sidebar.slider('Please enter your travel time in minutes', min_value= df.travtime.min(), max_value= df.travtime.max(), step= 1)
car_use = st.selectbox('PLease provid your car usage', df.car_use.unique())
bluebook = st.number_input('Please provide your car value', min_value= df.bluebook.min(), max_value= df.bluebook.max())
tif = st.sidebar.slider('Loyalty years', min_value= df.tif.min(), max_value= df.tif.max(), step= 1)
car_type = st.selectbox('PLease provid your car type', df.car_type.unique())
red_car = st.selectbox('Red car or Not', df.red_car.unique())
oldclaim = st.number_input('Please provide your old claim amount', min_value= df.oldclaim.min(), max_value= df.oldclaim.max())
clm_freq = st.sidebar.slider('Please provide number of previous claims', min_value= df.clm_freq.min(), max_value= df.clm_freq.max(), step= 1)
revoked = st.selectbox('License Revoked within 7 years', df.revoked.unique())
mvr_pts = st.sidebar.slider('Please provide vechile record points', min_value= df.mvr_pts.min(), max_value= df.mvr_pts.max(), step= 1)
clm_amt = st.number_input('Please provide your total claims amount', min_value= df.clm_amt.min(), max_value= df.clm_amt.max())
car_age = st.sidebar.slider('Please enter your car age', min_value= int(df.car_age.min()), max_value= int(df.car_age.max()), step= 1)
urbanicity = st.selectbox('Urbanicity', df.urbanicity.unique())

# Import Model
Model = joblib.load('knn.pkl')

input_cols = df.columns.drop('claim_flag')

new_data = pd.DataFrame(columns= input_cols, data= [ [kidsdriv, age, homekids, yoj, income, parent1, home_val,
                                           mstatus, gender, education, occupation, travtime, car_use,
                                           bluebook, tif, car_type, red_car, oldclaim, clm_freq,
                                           revoked, mvr_pts, clm_amt, car_age, urbanicity] ])

if st.button('Predict'):

    result = Model.predict(new_data)[0]

    if result == 0:
        st.write('Claim Flag : NO')

    else:
        st.write('Claim Flag : YES')
