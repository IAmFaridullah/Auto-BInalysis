from django.shortcuts import render,redirect
from django.http import HttpResponse, FileResponse
from analysis import utils
import os
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import io
from io import BytesIO
from fpdf import FPDF

from django.core.files import File
from wsgiref.util import FileWrapper
from analysis import Testing_models
# Create your views here.
from analysis.models import TrainedModel
# def train_model(request):

        
@csrf_exempt
def user_models(request):
    print('check')
    if request.method == 'POST':
        # replace 'my_username' with the username you want to filter on
        queryset = TrainedModel.objects.filter(username='muzamil')
        # loop through the queryset and print each object
        users_data = [{'username': obj.username, 'model_name': obj.model_name,
                        'path': obj.model_path} for obj in queryset]

        # for obj in queryset:
        #     print(obj)
            
        return HttpResponse(users_data)


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
        
        
import os
from django.http import FileResponse

from django.http import HttpResponse

@csrf_exempt

def test_model(request):
    if request.method == 'POST':
        dataset = request.FILES.get('file')
        username = request.POST['username']
        model_name = request.POST['model_name']
        model_dir = os.path.join(
        'analysis', 'trained-models', f'user_{username}', model_name)
        # model_dir = 'trained-models\\user_muzamil\\Member Churn.pkl'
        df = Testing_models.test_models(dataset, model_dir)
        file_path = 'analysis\\Tested_file\\output.xlsx'
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response


@csrf_exempt
def download_file(request, file_path):
    # Get the file name from the file path
    file_name = os.path.basename(file_path)

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Set the response headers
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response
# @csrf_exempt
# def download_file(request):
#     # Path to the file on the server
#     file_path = 'C:\\Users\\Flatmates.Org\\Desktop\\Auto-BInalysis-Project\\Auto_Binalysis_Backend\\analysis\\Tested_file\\output.xlsx'
#     # Open the file in binary mode
#     file = open(file_path, 'rb')
#     # Use Django's FileResponse to send the file to the client
#     response = FileResponse(file)
#     # Set the content type and the content-disposition headers
#     response['content_type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)
#     return response

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

        # model_name = f'model_{dataset.name.split(".")[0]}.csv'
        # file_path = os.path.join(user_dir, model_name)
        # with open(file_path, 'wb+') as destination:
        #     for chunk in dataset.chunks():
        #         destination.write(chunk)
