from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
from analysis import utils
import os
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import io
import json
from django.core.files import File
from wsgiref.util import FileWrapper
from analysis import Testing_models
# Create your views here.
from analysis.models import TrainedModel
# def train_model(request):


@csrf_exempt
def user_models(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']
        print(username)
        queryset = TrainedModel.objects.filter(username=username)
        models_data = [{'username': obj.username, 'model_name': obj.model_name,
                       'path': obj.model_path, 'accuracy': obj.accuracy} for obj in queryset]

        return JsonResponse({'models_data': models_data}, status=200)


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
        check = utils.training_models(dataset, username)
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
        model_name = request.POST['model_name']
        print("model_name :", model_name)
        model_dir = 'trained-models\\user_muzamil\\Member Churn.pkl'
        df = Testing_models.test_models(dataset, model_dir)
        # write the DataFrame to an Excel file in memory
        excel_file = io.BytesIO()
        with pd.ExcelWriter(excel_file) as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

        # create an HttpResponse object with the Excel file as the content
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        # response['Content-Disposition'] = 'attachment; filename=test_model_output.xlsx'
        response['Content-Disposition'] = 'attachment; filename="test_model_output.xlsx"; filename*=UTF-8\'\'test_model_output.xlsx'

        response.write(excel_file.getvalue())

        return response

# @csrf_exempt
# def test_model(request):
#     if request.method == 'POST':
#         dataset = request.FILES.get('file')
#         username = request.POST['username']
#         model_dir = 'trained-models\\user_muzamil\\Member Churn.pkl'
#         df=Testing_models.test_models(dataset,model_dir)
#         # write the DataFrame to an Excel file in memory
#         print(type(df))
#         excel_file = io.BytesIO()
#         with pd.ExcelWriter(excel_file) as writer:
#             df.to_excel(writer, index=False, sheet_name='Sheet1')

#         # create an HttpResponse object with the Excel file as the content
#         response = HttpResponse(
#             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )
#         response['Content-Disposition'] = 'attachment; filename=my_excel_file.xlsx'
#         response.write(excel_file.getvalue())

#         return response


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
