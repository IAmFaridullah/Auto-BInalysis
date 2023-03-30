import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle
# import pdfkit


def pharms():

    # Load the dataset
    df = pd.read_csv('PharmaSalesWeekly.csv')

    # convert the 'Week( Starting date)' column to date format
    df['Week( Starting date)'] = pd.to_datetime(df['Week( Starting date)'])

    # Define the date range for predictions
    # future = pd.date_range(start='2023-03-27', periods=52, freq='W')
    dates=df.columns[1:]
    # Create separate models for each medication
    models = {}
    for col in df.columns[1:]:
        # Fit an ARIMA model to the data
        model = ARIMA(df[col], order=(1, 0, 0))
        model_fit = model.fit()
        # Add the trained model to the dictionary of models
        models[col] = model_fit

    # # Generate predictions for each medication
    # predictions = pd.DataFrame({'ds': future})
    # for col, model in models.items():
    #     # Make predictions using the trained model
    #     forecast = model.predict(start=len(df), end=len(df)+51)
    #     # Add the predictions to the output dataframe
    #     predictions[col] = forecast.values

    # Print the predictions
    # print(predictions.head())
    # save the model to a file using pickle
    filename = 'data\\PharmaSalesWeekly.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    # print(dates)
    return dates
        
        

def model_load(dates):
    filename = 'data\\PharmaSalesWeekly.pkl'
    with open(filename, 'rb') as file:
        loaded_models = pickle.load(file)

    # Define the date range for predictions
    future = pd.date_range(start='2023-03-28', periods=52, freq='W')

    # Generate predictions for each medication using the loaded models
    predictions = pd.DataFrame({'ds': future})
    for col in dates:
        # Get the corresponding trained ARIMA model from the dictionary
        loaded_model = loaded_models[col]
        # Make predictions using the trained model
        forecast = loaded_model.predict(start=len(dates), end=len(dates)+51)
        # Add the predictions to the output dataframe
        predictions[col] = forecast.values
        print(predictions)

if __name__ == '__main__':
    dates = pharms()
    # model_load(dates)
    

# # Create a sample dataframe
# df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

# # Convert the dataframe to HTML
# html = df.to_html()

# # Generate the PDF file
# pdfkit.from_string(html, 'output.pdf')