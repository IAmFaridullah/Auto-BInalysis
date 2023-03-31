import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle
from django.http import HttpResponse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def saving_model(dataset,file_name,model):
        # save the model to a file using pickle
        model_name = f'{dataset.name.split(".")[0]}.pkl'
        print(model_name)
        filename = f'analysis\\trained-models\\user_{file_name}\\{model_name}'  # trained-models
        with open(filename, 'wb') as file:
            pickle.dump(model, file)


def member_churn(dataset,file_name):
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
        print("Accuracy:", accuracy_score(y_test, rf_pred))

        #Saving Model
        saving_model(dataset,file_name,churn_model)
        return 'Done'


def PharmaSalesWeekly(dataset,file_name):

        # Load the dataset
        print(file_name)
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

        # Print the predictions
        print(predictions.head())

        #Saving Model
        saving_model(dataset,file_name,model)
        return 'Done'


    
def Member_Card_Analysis_Data(dataset,file_name):

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

        #Saving Model
        saving_model(dataset,file_name,card_model)
        return 'Done'