import pandas as pd
from analysis import Training_models
from analysis import Testing_models
import os

def training_models(dataset,file_name):
    if dataset.name.split(".")[0] == 'PharmaSalesWeekly':
        status=Training_models.PharmaSalesWeekly(dataset,file_name)
        if status == 'Done':
            return 'Done'
        else:
            return 'error'

    elif dataset.name.split(".")[0] == 'Member Churn':
        status=Training_models.member_churn(dataset,file_name)
        if status == 'Done':
            return 'Done'
        # return 'Done'

    elif dataset.name.split(".")[0] == 'Member Card Analysis Data':
        status=Training_models.Member_Card_Analysis_Data(dataset,file_name)
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