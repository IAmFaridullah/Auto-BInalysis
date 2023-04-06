import pickle
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.files import File
from wsgiref.util import FileWrapper
import io
import os
def test_models(dataset,model_dir):

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

    filename ='C:\\Users\\Flatmates.Org\\Desktop\\Auto-BInalysis-Project\\Auto_Binalysis_Backend\\analysis\\trained-models\\user_muzamil\\Member Churn.pkl'
    with open(filename, 'rb') as file:
        loaded_models = pickle.load(file)
        prediction=loaded_models.predict(df)
        # print(prediction)
        df = df.assign(Churn_predict = np.where(prediction == 1, 'Yes', 'No'))
        df['HomeDelivery'] = df['HomeDelivery'].map({0: 'No', 1: 'Yes'})
        df['SilverCard'] = df['SilverCard'].map({0: 'No', 1: 'Yes'})
        df['GoldenCard'] = df['GoldenCard'].map({0: 'No Silver Card',-1 : 'No', 1: 'Yes'})  #'Yes': 1, 'No': -1, 'No Silver Card':0
        df['gender'] = df['gender'].map({0: 'Female', 1: 'Male'})
        df.insert(0, 'Customer ID', customerID)

        print(df.head(15))

        df.to_excel(f'analysis\\Tested_file\\output.xlsx', index=False)

        # write the DataFrame to an Excel file in memory
        
        return df