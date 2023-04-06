import pickle
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.files import File
from wsgiref.util import FileWrapper
import io
import os
from statsmodels.tsa.arima.model import ARIMA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def test_models(dataset,model_dir):
    dataset_name = dataset.name.split(".")[0] 
    if dataset_name == 'MemberChurnTest':
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

    elif dataset_name == 'MemberCardAnalysisTest':
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

    elif dataset_name == 'PharmaTest':
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

    elif dataset_name == 'DailyMobOrderTest':
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

    elif dataset_name =='DailySalesToothpastesTest':
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

    elif dataset_name =='ChaklalaStoreSalesTest':
        df = pd.read_excel(dataset)
        # Convert the "Product Name" column into a numerical representation
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(df['Product Name'])

        # Perform clustering using K-Means algorithm
        k = 3  # number of clusters
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)

        # Assign each product to its corresponding cluster
        df['Cluster'] = kmeans.labels_

        # Create a mapping between invoice numbers and their respective clusters
        mapping = df[['Inv No', 'Cluster']].drop_duplicates().set_index('Inv No')['Cluster'].to_dict()

        # Group products based on their invoice numbers
        grouped_df = df.groupby(['Inv No'])['Product Name'].apply(list).reset_index()

        # Add a new column with the corresponding cluster for each invoice number
        grouped_df['Cluster'] = grouped_df['Inv No'].map(mapping)

        # Print the resulting groups
        print(grouped_df)
        return grouped_df


    else:
        return pd.DataFrame({'error','Wrong dataset'})