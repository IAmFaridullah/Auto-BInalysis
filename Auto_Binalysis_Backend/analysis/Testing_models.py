import pickle
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.files import File
from wsgiref.util import FileWrapper
import io
import os
from statsmodels.tsa.arima.model import ARIMA

def test_models(dataset,model_dir):
    dataset_name = dataset.name.split(".")[0] 
    if dataset_name == 'Member Churn':
        df = pd.read_excel(dataset)
        # Convert the categorical variable to numerical values
        df['HomeDelivery'] = df['HomeDelivery'].map({'Yes': 1, 'No': 0})
        df['SilverCard'] = df['SilverCard'].map({'Yes': 1, 'No': 0})
        df['GoldenCard'] = df['GoldenCard'].map({'Yes': 1, 'No': -1, 'No Silver Card':0})
        df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
        customerID = df['customerID']
        # Drop the customerID column
        df = df.drop('customerID', axis=1)
        # filling missing values
        df = df.dropna()
        with open(model_dir, 'rb') as file:
            loaded_models = pickle.load(file)
            prediction=loaded_models.predict(df)
            df = df.assign(Churn_predict = np.where(prediction == 1, 'Yes', 'No'))
            df['HomeDelivery'] = df['HomeDelivery'].map({0: 'No', 1: 'Yes'})
            df['SilverCard'] = df['SilverCard'].map({0: 'No', 1: 'Yes'})
            df['GoldenCard'] = df['GoldenCard'].map({0: 'No Silver Card',-1 : 'No', 1: 'Yes'})  #'Yes': 1, 'No': -1, 'No Silver Card':0
            df['gender'] = df['gender'].map({0: 'Female', 1: 'Male'})
            df.insert(0, 'Customer ID', customerID)
            testfile = os.path.join(
                'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
            # write the DataFrame to an Excel file in memory
            df.to_excel(testfile, index=False)
            return df

    elif dataset_name == 'Member_Card_Analysis_Data':
        # Load the data into a pandas DataFrame
        df = pd.read_excel(dataset)
        # Convert the categorical variable to numerical values
        df['RecentCardRenewal'] = df['RecentCardRenewal'].map({'Yes': 1, 'No': 0})
        AccountID = df['AccountID']
        # Drop the 'AccountID' column
        df = df.drop('AccountID', axis=1)
        # filling missing values
        df = df.dropna()
        with open(model_dir, 'rb') as file:
            loaded_models = pickle.load(file)
            prediction=loaded_models.predict(df)
            df = df.assign(Churn_predict = np.where(prediction == 1, 'Yes', 'No'))
            df.insert(0, 'Account ID', AccountID)
            testfile = os.path.join(
                'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
            # write the DataFrame to an Excel file in memory
            df.to_excel(testfile, index=False)
            return df

    elif dataset_name == 'PharmaSalesWeekly':
        # Generate predictions for each medication using the loaded models

        predictions = pd.read_excel(dataset)
        # Load the saved models from file using pickle

        with open(model_dir, 'rb') as file:
            loaded_models = pickle.load(file)
        print(type(loaded_models))
        for col in predictions.columns[1:]:
            # Get the corresponding trained ARIMA model from the dictionary
            loaded_model = loaded_models[col]
            # Make predictions using the trained model
            forecast = loaded_model.predict(start=len(predictions), end=len(predictions)+51)
            
            # Add the predictions to the output dataframe
            predictions[col] = forecast.values
            
        testfile = os.path.join(
            'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
        # write the DataFrame to an Excel file in memory
        predictions.to_excel(testfile, index=False)
        return predictions

    elif dataset_name == 'Daily Orders for Mobile Accessories 2020-2022':
            # Generate predictions for each medication using the loaded models

            predictions = pd.read_excel(dataset)
            # Load the saved models from file using pickle

            with open(model_dir, 'rb') as file:
                loaded_models = pickle.load(file)
            print(type(loaded_models))
            for col in predictions.columns[1:]:
                # Get the corresponding trained ARIMA model from the dictionary
                loaded_model = loaded_models[col]
                # Make predictions using the trained model
                forecast = loaded_model.predict(start=len(predictions), end=len(predictions)+51)
                
                # Add the predictions to the output dataframe
                predictions[col] = forecast.values
                
            testfile = os.path.join(
                'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
            # write the DataFrame to an Excel file in memory
            predictions.to_excel(testfile, index=False)
            return predictions

    elif dataset_name =='Daily Sales Toothpastes':
            # Generate predictions for each medication using the loaded models
            predictions = pd.read_excel(dataset)
            # Load the saved models from file using pickle

            with open(model_dir, 'rb') as file:
                loaded_models = pickle.load(file)
            print(type(loaded_models))
            for col in predictions.columns[1:]:
                # Get the corresponding trained ARIMA model from the dictionary
                loaded_model = loaded_models[col]
                # Make predictions using the trained model
                forecast = loaded_model.predict(start=len(predictions), end=len(predictions)+51)
                
                # Add the predictions to the output dataframe
                predictions[col] = forecast.values
                
            testfile = os.path.join(
                'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
            # write the DataFrame to an Excel file in memory
            predictions.to_excel(testfile, index=False)
            return predictions

    # elif dataset_name =='Chaklala Store Sales':
        