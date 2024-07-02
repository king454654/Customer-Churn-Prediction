import streamlit as st
import pickle
import pandas as pd

gender=['Female','Male']
SeniorCitizen_output=['Yes','No']
yes_No=['Yes','No']
MultipleLines_output=['Yes','No','No phone service']
InternetService_output=['DSL', 'Fiber optic', 'No']
OnlineSecurity_output=['Yes','No','No internet service']
Contract_output=['Month-to-month' ,'One year' ,'Two year']
PaymentMethod_output=['Electronic check' ,'Mailed check' ,'Bank transfer (automatic)', 'Credit card (automatic)']

st.title("Customer Churn Prediction")

col1,col2,col3,col4,col5,col6 = st.columns(6)
col12,col22,col32,col42,col52,col62 = st.columns(6)
col13,col23,col33,col43 = st.columns(4)

with col1:
    gender = st.selectbox('Select Gender', gender)
with col2:
    SeniorCitizen = st.selectbox('Senior Citizen',SeniorCitizen_output)
with col3:
    Partner = st.selectbox('Partner', yes_No)
with col4:
    Dependents = st.selectbox('Dependents', yes_No)
with col5:
    PhoneService = st.selectbox('Phone Service', yes_No)
with col6:
    MultipleLines = st.selectbox('Multiple Lines', MultipleLines_output)
with col12:
    InternetService=st.selectbox('Internet Service',InternetService_output)
with col22:
    OnlineSecurity=st.selectbox('Online Security',OnlineSecurity_output)
with col32:
    OnlineBackup=st.selectbox('Online Backup',OnlineSecurity_output)
with col42:
    DeviceProtection=st.selectbox('Device Protection',OnlineSecurity_output)
with col52:
    TechSupport=st.selectbox('Tech Support',OnlineSecurity_output)
with col62:
    StreamingTV=st.selectbox('Streaming TV',OnlineSecurity_output)
with col43:
    StreamingMovies=st.selectbox('Streaming Movies',OnlineSecurity_output)
with col13:
    Contract = st.selectbox('Contract',Contract_output)
with col23:
    PaperlessBilling = st.selectbox('Paperless Billing',yes_No)
with col33:
    PaymentMethod = st.selectbox('Payment Method',PaymentMethod_output)

MonthlyCharges=st.number_input('Monthly Charges')
TotalCharges=st.number_input('Total Charges')


pipe=pickle.load(open('model.pickle','rb'))
model_prediction=pickle.load(open('model_prediction.pickle','rb'))
if st.button('Prediction'):
    # pass
    input_df=pd.DataFrame({'gender':[gender] ,'SeniorCitizen': [1 if SeniorCitizen == 'Yes' else 0], 'Partner':[Partner], 'Dependents':[Dependents], 'PhoneService':[PhoneService],
       'MultipleLines': [MultipleLines], 'InternetService':[InternetService], 'OnlineSecurity':[OnlineSecurity], 'OnlineBackup':[OnlineBackup],
       'DeviceProtection':[DeviceProtection], 'TechSupport':[TechSupport], 'StreamingTV':[StreamingTV], 'StreamingMovies': [StreamingMovies],
       'Contract':[Contract], 'PaperlessBilling':[PaperlessBilling], 'PaymentMethod':[PaymentMethod], 'MonthlyCharges': [MonthlyCharges],
       'TotalCharges' : [TotalCharges]})

    # st.table(input_df)
    result=pipe.predict(input_df)
    YesOrNo=model_prediction.inverse_transform(result)
    st.header(str(YesOrNo[0])+' Customer Churn.')
