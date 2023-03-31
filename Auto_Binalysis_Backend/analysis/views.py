from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from analysis import utils
import os
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# Create your views here.

# def train_model(request):
    
@csrf_exempt
def train_model(request):
    if request.method == 'POST':
        dataset = request.FILES.get('file')
        username = request.POST['username']

        # print('file name:', dataset.name)
        # df = pd.read_csv(dataset)
        # print(df.head())
        user_dir = os.path.join(
            'analysis', 'trained-models', f'user_{username}')
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        check=utils.training_models(dataset,username)
        # model_name = f'model_{dataset.name.split(".")[0]}.csv'
        # file_path = os.path.join(user_dir, model_name)
        # with open(file_path, 'wb+') as destination:
        #     for chunk in dataset.chunks():
        #         destination.write(chunk)
        
        if check == 'Done':
            return HttpResponse('Dataset is uploaded correctly')
        else:
            return HttpResponse('Wrong Dataset')
        
@csrf_exempt
def test_model(request):
    if request.method == 'POST':
        dataset = request.FILES.get('file')
        username = request.POST['username']
        check=utils.Testing_model(dataset,username)

        if check == 'Done':
            return HttpResponse('Testing')
    
    

@csrf_exempt
def dataset_upload(request):
    if request.method == 'POST':
        dataset = request.FILES.get('file')
        username = request.POST['username']
        print('file name:', dataset.name)
        df = pd.read_csv(dataset)
        print(df.head())
        user_dir = os.path.join(
            'chatbot', 'trained-models', f'user_{username}')
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        model_name = f'model_{dataset.name.split(".")[0]}.csv'
        file_path = os.path.join(user_dir, model_name)
        with open(file_path, 'wb+') as destination:
            for chunk in dataset.chunks():
                destination.write(chunk)
