import pickle
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.files import File
from wsgiref.util import FileWrapper
import io
from sklearn.preprocessing import LabelEncoder
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

    elif dataset_name =='KitchenItemSalesTest':
        df = pd.read_excel(dataset)
        # Convert the "Product Name" column into a numerical representation
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(df['Items'])

        # Perform clustering using K-Means algorithm
        k = 3  # number of clusters
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)

        # Assign each product to its corresponding cluster
        df['Cluster'] = kmeans.labels_

        # Create a mapping between invoice numbers and their respective clusters
        mapping = df[['TransactionNo', 'Cluster']].drop_duplicates().set_index('TransactionNo')['Cluster'].to_dict()

        # Group products based on their invoice numbers
        grouped_df = df.groupby(['TransactionNo'])['Items'].apply(list).reset_index()

        # Add a new column with the corresponding cluster for each invoice number
        grouped_df['Cluster'] = grouped_df['TransactionNo'].map(mapping)

        # Print the resulting groups
        print(grouped_df)
        return grouped_df

    elif dataset_name =='WomenDressSalesTest':
        df = pd.read_excel(dataset)
        # Convert the "Product Name" column into a numerical representation
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(df['item'])

        # Perform clustering using K-Means algorithm
        k = 3  # number of clusters
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)

        # Assign each product to its corresponding cluster
        df['Cluster'] = kmeans.labels_

        # Create a mapping between invoice numbers and their respective clusters
        mapping = df[['OrderNo', 'Cluster']].drop_duplicates().set_index('OrderNo')['Cluster'].to_dict()

        # Group products based on their invoice numbers
        grouped_df = df.groupby(['OrderNo'])['item'].apply(list).reset_index()

        # Add a new column with the corresponding cluster for each invoice number
        grouped_df['Cluster'] = grouped_df['OrderNo'].map(mapping)

        # Print the resulting groups
        print(grouped_df)
        return grouped_df

    elif dataset_name == 'MonthlySalesTablewareTest':
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

    elif dataset_name =='MobileAccessoriesDataTest':
        df = pd.read_excel(dataset)
        # Convert the "Product Name" column into a numerical representation
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(df['item'])

        # Perform clustering using K-Means algorithm
        k = 3  # number of clusters
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)

        # Assign each product to its corresponding cluster
        df['Cluster'] = kmeans.labels_

        # Create a mapping between invoice numbers and their respective clusters
        mapping = df[['Member_number', 'Cluster']].drop_duplicates().set_index('Member_number')['Cluster'].to_dict()

        # Group products based on their invoice numbers
        grouped_df = df.groupby(['Member_number'])['item'].apply(list).reset_index()

        # Add a new column with the corresponding cluster for each invoice number
        grouped_df['Cluster'] = grouped_df['Member_number'].map(mapping)

        # Print the resulting groups
        print(grouped_df)
        return grouped_df

    elif dataset_name == 'ChaklalaStoreSalesTest':
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

    elif dataset_name == 'PharmaDataNovemberTest':
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
        mapping = df[['Inv #', 'Cluster']].drop_duplicates().set_index('Inv #')['Cluster'].to_dict()

        # Group products based on their invoice numbers
        grouped_df = df.groupby(['Inv #'])['Product Name'].apply(list).reset_index()

        # Add a new column with the corresponding cluster for each invoice number
        grouped_df['Cluster'] = grouped_df['Inv #'].map(mapping)

        # Print the resulting groups
        print(grouped_df)
        return grouped_df

    elif dataset_name == 'Phase8ReportDectTest':
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
        mapping = df[['Inv #', 'Cluster']].drop_duplicates().set_index('Inv #')['Cluster'].to_dict()

        # Group products based on their invoice numbers
        grouped_df = df.groupby(['Inv #'])['Product Name'].apply(list).reset_index()

        # Add a new column with the corresponding cluster for each invoice number
        grouped_df['Cluster'] = grouped_df['Inv #'].map(mapping)

        # Print the resulting groups
        print(grouped_df)
        return grouped_df

    elif dataset_name == 'RwpandIsbCustomersServiceTest':
        df = pd.read_csv(dataset)
        # Preprocess the data
        # Convert the categorical variable to numerical values
        if set(df['PurchaseInEveryMonth'].dropna().unique()) == {'Yes', 'No'}:
            df['PurchaseInEveryMonth'] = df['PurchaseInEveryMonth'].map({'Yes': 1, 'No': 0})
        if set(df['ECard'].dropna().unique()) == {'Yes', 'No'}:
            df['ECard'] = df['ECard'].map({'Yes': 1, 'No': 0})
        if set(df['Churn'].dropna().unique()) == {'Yes', 'No'}:
            df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
        if set(df['Gender'].dropna().unique()) == {'Male', 'Female'}:
            df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
        customerID = df['customerAccountID']
        # Drop the 'AccountID' column
        df = df.drop('CustomerAccountID', axis=1)
        # filling missing values
        df = df.dropna()
        df['TotalPointsGained'] = df['TotalPointsGained'].astype(int)
        df['Age'] = df['Age'].astype(int)
        df['TenureInYears'] = df['TenureInYears'].astype(int)
        df['BranchesVisited'] = df['BranchesVisited'].astype(int)
        le = LabelEncoder()
        df['AccountBranch_Encoded'] = le.fit_transform(df['AccountBranch'])
        # Drop the 'AccountBranch' column
        df = df.drop('AccountBranch', axis=1)
        with open(model_dir, 'rb') as file:
            loaded_models = pickle.load(file)
            prediction=loaded_models.predict(df)
            df = df.assign(Churn_predict = np.where(prediction == 1, 'Yes', 'No'))
            df['PurchaseInEveryMonth'] = df['PurchaseInEveryMonth'].map({'No': 0, 'Yes': 1})
            df['ECard'] = df['ECard'].map({'No': 0, 'Yes': 1})
            # df['GoldenCard'] = df['GoldenCard'].map({0: 'No Silver Card',-1 : 'No', 1: 'Yes'})  #'Yes': 1, 'No': -1, 'No Silver Card':0
            df['gender'] = df['gender'].map({0: 'Female', 1: 'Male'})
            df.insert(0, 'CustomerAccountID', customerID)
            
            testfile = os.path.join(
                'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
            # write the DataFrame to an Excel file in memory
            df.to_excel(testfile, index=False)
            return df
    
    elif dataset_name == 'WomenClothingReviewsTest':
        print('wait')
        df = pd.read_excel(dataset)
        Order = df['Order_ID']
        # drop unnecessary columns
        df = df.drop(['Order_ID', 'Would_Recommended'], axis=1)
        df.dropna(inplace=True)

        le = LabelEncoder()
        df['Product_Class_Encoded'] = le.fit_transform(df['Product_Class'])
        # Drop the 'Product_Class' column
        df = df.drop('Product_Class', axis=1)

            # Load the model for testing
        with open(model_dir, 'rb') as f:
            loaded_model = pickle.load(f)
            prediction=loaded_model.predict(df)

            # Assuming you have the encoded column 'Product_Class_Encoded' in your DataFrame
            df['Product_Class'] = le.inverse_transform(df['Product_Class_Encoded'])
            df = df.assign(Rating = prediction) 
            df.insert(0, 'Order ID', Order)
            df = df.drop('Product_Class_Encoded', axis=1)

            testfile = os.path.join(
                'analysis', 'Tested_file', f'{dataset_name}_output.xlsx')
            df.to_excel(testfile, index=False)
            return df

    else:
        return pd.DataFrame({'error','Wrong dataset'})