import pandas as pd
from analysis import Training_models
from analysis import Testing_models
import os


def training_models(dataset, username):
    if dataset.name.split(".")[0] == 'PharmaSalesWeekly':
        status = Training_models.PharmaSalesWeekly(dataset, username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == 'Member Churn':
        status = Training_models.member_churn(dataset, username)
        if status == 'Done':
            return 'Done'
        # return 'Done'

    elif dataset.name.split(".")[0] == 'Member Card Analysis Data':
        status = Training_models.Member_Card_Analysis_Data(dataset, username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == 'Daily Orders Mob Acc':
        status = Training_models.Daily_Orders_for_Mobile_Accessories(dataset, username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == 'Chaklala Store Sales':
        status = Training_models.Chaklala_Store_Sales(dataset, username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == 'Daily Sales Toothpastes':
        status = Training_models.Daily_Sales_Toothpastes(dataset, username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Women's Clothing Reviews":
        status = Training_models.Womens_Clothing_Reviews(dataset,username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Rwp and Isb Customers Service data":
        status = Training_models.Rwp_Isb_Customers_Service(dataset,username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Monthly Sales Tableware":
        status = Training_models.Monthly_Sales_tableware(dataset,username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Pharma-Data-November-22":
        status = Training_models.Pharma_Data_November(dataset,username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Phase 8 Report dec 2022":
        status = Training_models.Phase_8_Report_dec_2022(dataset,username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Kitchen Item Sales":
        status = Training_models.Kitchen_Item_Sales(dataset,username)
        if status == 'Done':
            return 'Done'
    
    elif dataset.name.split(".")[0] == "Women Dress Sales Jan - March 2023":
        status = Training_models.Women_Dress_Sales_Jan(dataset,username)
        if status == 'Done':
            return 'Done'

    elif dataset.name.split(".")[0] == "Mobile Accessories Data per Customer":
        status = Training_models.Mobile_Accessories_Data_per_Customer(dataset,username)
        if status == 'Done':
            return 'Done'

    # elif dataset.name.split(".")[0] == "Supermart Punjab and Isb Sales_Updated":
        # status = Training_models.Supermart_Punjab_and_Isb_Sales_Updated(dataset,username)
        # if status == 'Done':
        #     return 'Done'

    else:
        return 'Wrong Dataset'


def Testing_model(dataset, username):
    dataset_name = dataset.name.split(".")[0]
    print(username)
    print(dataset_name)

    model_dir = os.path.join(
        'analysis', 'trained-models', f'user_{username}', f'{dataset_name}.pkl')
    if os.path.exists(model_dir):
        Testing_models.test_models(dataset, model_dir)
        print(model_dir)
        return 'Done'
    else:
        return 'error'
