# Import libraries
import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = 'http://backend:7860'

# Set the title of the app
st.title('SuperKart Sales Predictor')

# Section for online prediction
st.subheader('Online Prediction')

# User input section
Product_Weight = st.number_input('Product Weight', min_value=0.0, value = 10.00)
Product_Sugar_Content = st.selectbox('Product Sugar Content', ['Low Sugar','Regular','No Sugar'])
Product_Allocated_Area = st.number_input('Product Allocated Area', min_value=0.0, value=0.025)
Product_Type = st.selectbox('Product Type', ['meat','snack foods','hard drinks','dairy','canned','soft drinks','health and hygiene','baking goods','bread','breakfast','frozen foods','fruits and vegetables','household','seafood','starchy foods','others'])
Product_MRP = st.number_input('Product MRP', min_value=0.0, value =150.0)
Store_Size = st.selectbox('Store Size', ['High','Medium','Low'])
Store_Location_City_Type = st.selectbox('Store Location City Type', ['Tier 1','Tier 2','Tier 3'])
Store_Type = st.selectbox('Store Type', ['Departmental Store','Supermarket Type 1','Supermarket Type 2','Food Mart'])
Cat_Id = st.selectbox('Cat Id', ['FD','DR','NC'])

# Create a dictionary with user inputs
product_data = pd.DataFrame([{
    'Product_Weight': Product_Weight,
    'Product_Sugar_Content': Product_Sugar_Content,
    'Product_Allocated_Area': Product_Allocated_Area,
    'Product_Type': Product_Type,
    'Product_MRP': Product_MRP,
    'Store_Size': Store_Size,
    'Store_Location_City_Type': Store_Location_City_Type,
    'Store_Type': Store_Type,
    'Cat_Id': Cat_Id,
}])

# Code for a Button and making a prediction
if st.button('Predict Sales', type='primary'):
  response = requests.post(f'{BACKEND_URL}/predict', json=product_data)
  if response.status_code == 200:
    prediction = response.json()['Predicted Sales (in dollars)']
    st.success(f'Predicted Sales: {prediction}')
  else:
    st.error('Error making prediction')


#Code for Batch predition
st.subheader('Batch Prediction')

# Allow for user uploaded CSV file
if uploaded_file is not None:
  response = requests.post(f'{BACKEND_URL}/batchpredict', files= {'file': uploaded_file})
  if response.status_code == 200:
    prediction = response.json()
    st.write(pd.DataFrame(prediction))
  else:
    st.error('Error making batch prediction')


