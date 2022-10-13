import streamlit as st
from utils import *

import numpy as np
import pandas as pd
import joblib

# import model
model = joblib.load('xgbpipe.joblib') # xgb classifier

st.title('Titanic App :ship:') # title of the app
# add all the customizable columns
passengerId = st.text_input('Input passenger ID', "123456") # input passenger id
passengerclass = st.select_slider('Choose the passenger class', [1,2,3]) # slider to select Pclass
name = st.text_input('Input passenger name', "John Smith")
gender = st.select_slider('Select the gender', ['male', 'female'])
age = st.slider('Input age', 0,100)
sibSp = st.slider('Input siblings', 0,10) # number of siblings or spouses
parch = st.slider('Input parents/children', 0,2) # number of parents/children aboard
ticket = st.number_input('Ticket number', 12345)
fare = st.number_input('Fare amount', 0,100)
cabin = st.text_input('Enter Cabin', "C52")
embarked = st.selectbox('Choose embarkation', ["S","C","Q"]) # C = Cherbourg, Q = Queenstown, S = Southampton

def predict():
    row = np.array([passengerId, passengerclass, 
                    name, gender, age, sibSp, 
                    parch, ticket, fare, cabin, embarked])
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)[0]
    if prediction == 1:
        st.success('Passenger survived :thumbsup:')
    else:
        st.error('Passenger did not survived :thumbsdown:')
        
st.button('Predict', on_click=predict)