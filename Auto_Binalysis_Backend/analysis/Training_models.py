import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle
from django.http import HttpResponse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from analysis.models import TrainedModel
from sklearn.metrics import mean_squared_error
import numpy as np


def save_model_to_db(model_name,username,accuracy,rmse,model_path):
    
        trained_model = TrainedModel(
        model_name=model_name,
        username=username,
        model_for='S1',
        accuracy=accuracy,
        rmse=rmse,
        model_path=model_path
        )
        trained_model.save()
        
def saving_model(dataset,username,model,accuracy,rmse): 
    # save the model to a file using pickle
    model_name = f'{dataset.name.split(".")[0]}.pkl'
    print(model_name)
    model_dir = os.path.join(
    'analysis', 'trained-models', f'user_{username}',f'{model_name}')
    print(model_dir)

    with open(model_dir, 'wb') as file:
        pickle.dump(model, file)
        
    save_model_to_db(model_name,username,accuracy,rmse,model_dir)


def member_churn(dataset,username):
    df = pd.read_excel(dataset)
    # Convert the categorical variable to numerical values
    df['HomeDelivery'] = df['HomeDelivery'].map({'Yes': 1, 'No': 0})
    df['SilverCard'] = df['SilverCard'].map({'Yes': 1, 'No': 0})
    df['GoldenCard'] = df['GoldenCard'].map({'Yes': 1, 'No': -1, 'No Silver Card':0})
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})

    # # Drop the customerID column
    df = df.drop('customerID', axis=1)
    # print(df.shape)
    # Convert the categorical variable to numerical values
    if set(df['Churn'].dropna().unique()) == {'Yes', 'No'}:
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # filling missing values
    df = df.dropna()

    # print(df.head(15))
    # Identify the strongest correlations with the "Churn" column
    corr_matrix = df.corr()
    churn_corr = corr_matrix['Churn'].sort_values(ascending=False)
    # print(churn_corr)
    
    features = df.loc[:, df.columns != 'Churn']
    
    X= features
    # select the target variable ('Churn' column)
    target = df['Churn']
    y= target
    # split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.1, random_state=42)

    # Train a Random Forest model
    churn_model = RandomForestClassifier(n_estimators=10)
    churn_model.fit(X_train, y_train)

    # Make predictions on the test set
    rf_pred = churn_model.predict(X_test)

    # Evaluate the models' performance
    print("\n Random Forest")
    accuracy = accuracy_score(y_test, rf_pred)
    print("Accuracy:", accuracy)
    #Saving Model    
    rmse = '0.1'
    saving_model(dataset,username,churn_model,accuracy,rmse)

    return 'Done'


def PharmaSalesWeekly(dataset,username):

    # Load the dataset
    print(username)
    df = pd.read_csv(dataset)
    # convert the 'Week( Starting date)' column to date format
    df['Week( Starting date)'] = pd.to_datetime(df['Week( Starting date)'])

    # Define the date range for predictions
    future = pd.date_range(start='2023-03-27', periods=52, freq='W')

    # Create separate models for each medication
    models = {}
    for col in df.columns[1:]:
        # Fit an ARIMA model to the data
        model = ARIMA(df[col], order=(1, 0, 0))
        model_fit = model.fit()
        # Add the trained model to the dictionary of models
        models[col] = model_fit

    # Generate predictions for each medication
    predictions = pd.DataFrame({'ds': future})
    for col, model in models.items():
        # Make predictions using the trained model
        forecast = model.predict(start=len(df), end=len(df)+51)
        # Add the predictions to the output dataframe
        predictions[col] = forecast.values
        # Calculate and print the RMSE
        actual = df[col][-52:].values
        predicted = forecast.values
    # mse = mean_squared_error(actual, predicted)
    # rmse = np.sqrt(mse)
    # print(f'RMSE for: {rmse}')
    # Print the predictions
    print(predictions.head())

    #Saving Model
    saving_model(dataset,username,models,accuracy=0.01,rmse=0.2)
    
    
    return 'Done'


    
def Member_Card_Analysis_Data(dataset,username):

    # Load the data into a pandas DataFrame
    df = pd.read_excel(dataset)
    # Convert the categorical variable to numerical values
    df['RecentCardRenewal'] = df['RecentCardRenewal'].map({'Yes': 1, 'No': 0})

    # Drop the 'AccountID' column
    df = df.drop('AccountID', axis=1)

    # Convert the categorical variable to numerical values
    if set(df['Churn'].dropna().unique()) == {'Yes', 'No'}:
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # filling missing values
    df = df.fillna(df.mean())

    # Identify the strongest correlations with the "Churn" column
    corr_matrix = df.corr()
    churn_corr = corr_matrix['Churn'].sort_values(ascending=False)

    # print(churn_corr)
    # Specify target variable
    target = 'Churn'
    y = df[target].astype(int)

    # Use all other columns as features
    X = df.drop(target, axis=1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    # Train a Random Forest model
    card_model = RandomForestClassifier()
    card_model.fit(X_train, y_train)

    # Make predictions on the test set
    rf_pred = card_model.predict(X_test)
    print(rf_pred)
    # Evaluate the models' performance
    print("\n Random Forest")
    print("Accuracy:", accuracy_score(y_test, rf_pred))
    accuracy = accuracy_score(y_test,rf_pred)
    rmse = 0.1
    #Saving Model
    saving_model(dataset,username,card_model,accuracy,rmse)
    
    return 'Done'

    

def Daily_Orders_for_Mobile_Accessories(dataset, username):
    print(username)
    # Load the data into a pandas DataFrame 
    df = pd.read_excel(dataset)

    # Remove column name 'Weekday'
    df = df.drop(['Weekday'], axis=1)

    df = df.dropna()

    # Check the summary statistics of the dataset
    print(df.describe())

    # Check for missing values
    print(df.isnull().sum())

    # Define the date range for predictions
    future = pd.date_range(start='2023-04-03', periods=52, freq='W')

    # Create separate models for each medication
    models = {}
    for col in df.columns[1:]:
        # Fit an ARIMA model to the data
        model = ARIMA(df[col], order=(1, 0, 0))
        model_fit = model.fit()
        # Add the trained model to the dictionary of models
        models[col] = model_fit

    # Generate predictions for each medication
    predictions = pd.DataFrame({'ds': future})
    for col, model in models.items():
        # Make predictions using the trained model
        forecast = model.predict(start=len(df), end=len(df)+51)
        # Add the predictions to the output dataframe
        predictions[col] = forecast.values

        # Calculate and print the RMSE
        actual = df[col][-52:].values
        predicted = forecast.values
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    print(f'RMSE for : {rmse}')

    # Print the predictions
    print(predictions.head())

    # Saving Model
    saving_model(dataset, username, models, accuracy=0.01, rmse=rmse)

    return 'Done'

'''    
# def Daily_Orders_for_Mobile_Accessories(dataset,username):
    print(username)
    # Load the data into a pandas DataFrame 
    df = pd.read_excel(dataset)
    # Remove column name 'Weekday'
    df = df.drop(['Weekday'], axis=1)
    df = df.dropna()
    # Check the summary statistics of the dataset
    print(df.describe())
    # Check for missing values
    print(df.isnull().sum())

    # Define the date range for predictions
    future = pd.date_range(start='2023-04-03', periods=52, freq='W')

    # Create separate models for each medication
    models = {}
    for col in df.columns[1:]:
        # Fit an ARIMA model to the data
        model = ARIMA(df[col], order=(1, 0, 0))
        model_fit = model.fit()
        # Add the trained model to the dictionary of models
        models[col] = model_fit

    # Generate predictions for each medication
    predictions = pd.DataFrame({'ds': future})
    for col, model in models.items():
        # Make predictions using the trained model
        forecast = model.predict(start=len(df), end=len(df)+51)
        # Add the predictions to the output dataframe
        predictions[col] = forecast.values

    # Print the predictions
    print(predictions.head())
    #Saving Model
    saving_model(dataset,username,models,accuracy=0.01,rmse=0.2)
    return 'Done'
'''
def Chaklala_Store_Sales(dataset,username):
    print(username)

    df = pd.read_excel(dataset)
    # Convert the "Product Name" column into a numerical representation
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['Product Name'])

    # Define a range of hyperparameters to search over
    param_grid = {
        "n_clusters": [2, 3, 4, 5, 6],
        "init": ["k-means++", "random"]
    }

    # Perform a grid search over the hyperparameters
    kmeans = KMeans(random_state=42)
    grid_search = GridSearchCV(
        kmeans, param_grid, cv=5, scoring='neg_mean_squared_error'
    )
    grid_search.fit(X)

    # Print the best hyperparameters and the corresponding evaluation metrics
    print("Best hyperparameters:", grid_search.best_params_)

    # Evaluate the clustering performance using alternative metrics
    labels = grid_search.best_estimator_.labels_
    silhouette = silhouette_score(X, labels)
    calinski_harabasz = calinski_harabasz_score(X.toarray(), labels)
    davies_bouldin = davies_bouldin_score(X.toarray(), labels)

    print("Silhouette Score:", silhouette)
    print("Calinski-Harabasz Score:", calinski_harabasz)
    print("Davies-Bouldin Score:", davies_bouldin)

    # Get the best estimator (i.e., the best model)
    best_model = grid_search.best_estimator_

    saving_model(dataset,username,best_model,silhouette,rmse = 0.1)
    # Predict the cluster assignments of the new data points
    # new_data_cluster_assignments = kmeans_model.predict(new_data)
    return 'Done'

def Daily_Sales_Toothpastes(dataset,username):
    print(username)
    df = pd.read_excel(dataset)
    # Define the date range for predictions
    future = pd.date_range(start='2023-04-03', periods=52, freq='W')

    # Create separate models for each medication
    models = {}
    for col in df.columns[1:]:
        # Fit an ARIMA model to the data
        model = ARIMA(df[col], order=(1, 0, 0))
        model_fit = model.fit()
        # Add the trained model to the dictionary of models
        models[col] = model_fit

    # Generate predictions for each medication
    predictions = pd.DataFrame({'ds': future})
    for col, model in models.items():
        # Make predictions using the trained model
        forecast = model.predict(start=len(df), end=len(df)+51)
        # Add the predictions to the output dataframe
        predictions[col] = forecast.values
        # Calculate and print the RMSE
        actual = df[col][-52:].values
        predicted = forecast.values
    mse = mean_squared_error(actual, predicted) 
    rmse = np.sqrt(mse)
    saving_model(dataset,username,models,accuracy=0.1,rmse=rmse)    
    return 'Done'