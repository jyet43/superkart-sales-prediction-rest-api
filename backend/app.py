
# Import libraries
import numpy as np
import pandas as pd
import joblib

from flask import Flask, request, jsonify

#Initialize the Flask application
superkart_predictor_api = Flask('SuperKart Sales Predictor')

# Load the trained model
model = joblib.load('deployment_files/superkart_sales_prediction_model_v1.0.joblib')

#Define a route for the homepage (GET request)
@superkart_predictor_api.route('/')
def home():
    return "Welcome to SuperKart Sales Predictor"

#Define an endpoint for a single prediction (POST request)
@superkart_predictor_api.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)

    # Input Data of 'Product_Sugar_Content', 'Product_Type', 'Store_Size', 'Store_Location_City_Type', 'Store_Type', 'Cat_Id', 'Product_Weight', 'Product_Allocated_Area', and 'Product_MRP'
    sample = {
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_Type': data['Product_Type'],
        'Product_MRP': data['Product_MRP'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type'],
        'Cat_Id': data['Cat_Id'],
    }

    # Convert the extracted data into a Pandas df
    input_data = pd.DataFrame([sample])

    # Make prediction
    prediction = model.predict(input_data).tolist()[0]

    # Return prediciton as a JSON response
    return jsonify({'Predicted Sales': prediction})


# Define an endpoint for batch prediction (POST request)
@superkart_predictor_api.route('/batchpredict', methods=['POST'])
def predict_rental_price_batch():
    # Get the uploaded CSV file from the request
    file = request.files['file']

    # Read the CSV file into a Pandas DataFrame
    input_data = pd.read_csv(file)

    # Make predictions for all properties in the DataFrame (get log_prices)
    predictions = model.predict(input_data).tolist()

    # Add predictions to the DataFrame
    input_data['Predicted_Sales'] = predictions

    # Convert the DataFrame to a dictionary
    output_dict = input_data.to_dict(orient='records')

    # Return the predictions dictionary as a JSON response
    return output_dict

# Run the Flask application
if __name__ == '__main__':
    superkart_predictor_api.run(debug=True)
