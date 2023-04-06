import pandas as pd
from analysis import Training_models
from analysis import Testing_models
import os


# # create a new TrainedModel instance
# trained_model = TrainedModel(
#     model_name='model1',
#     user='John Doe',
#     model_for=ModelForChoices.S1,
#     accuracy=0.95,
#     rmse=0.05,
#     model_path='/path/to/model1.pth'
# )

# # save the new instance to the database
# trained_model.save()


def training_models(dataset,username):
    if dataset.name.split(".")[0] == 'PharmaSalesWeekly':
        status=Training_models.PharmaSalesWeekly(dataset,username)
        
        if status == 'Done':
            return 'Done'
        else:
            return 'error'

    elif dataset.name.split(".")[0] == 'Member Churn':
        status=Training_models.member_churn(dataset,username)
        
        if status == 'Done':
            return 'Done'
        # return 'Done'

    elif dataset.name.split(".")[0] == 'Member Card Analysis Data':
        status=Training_models.Member_Card_Analysis_Data(dataset,username)
        if status == 'Done':
            return 'Done'
        
    elif dataset.name.split(".")[0] == 'Daily Orders for Mobile Accessories 2020-2022':
        status=Training_models.Daily_Orders_for_Mobile_Accessories(dataset,username)
        if status == 'Done':
            return 'Done'
        
    elif dataset.name.split(".")[0] == 'Chaklala Store Sales':
        status=Training_models.Chaklala_Store_Sales(dataset,username)
        if status == 'Done':
            return 'Done'
        
    elif dataset.name.split(".")[0] == 'Daily Sales Toothpastes':
        status=Training_models.Chaklala_Store_Sales(dataset,username)
        if status == 'Done':
            return 'Done'

    else:
        return 'Wrong Dataset'

def Testing_model(dataset,username):
    check = dataset.name.split(".")[0]
    print(username)
    print(check)

    model_dir = os.path.join(
    'analysis', 'trained-models', f'user_{username}',f'{check}.pkl')
    if os.path.exists(model_dir):
        Testing_models.test_models(dataset,model_dir)
        print(model_dir)
        return 'Done'
    else:
        return 'error'