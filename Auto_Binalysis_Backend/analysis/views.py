from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
from analysis import utils
import os
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import io
from django.core.files import File
from wsgiref.util import FileWrapper
from analysis import Testing_models
# Create your views here.
from analysis.models import TrainedModel
# def train_model(request):
import json


@csrf_exempt
def user_models(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']
        queryset = TrainedModel.objects.filter(username=username)
        models_data = [{'username': obj.username, 'model_name': obj.model_name,
                       'path': obj.model_path, 'accuracy': obj.accuracy, 'rmse': obj.rmse, 'silhouette': obj.silhouette} for obj in queryset]

        return JsonResponse({'models_data': models_data}, status=200)


@csrf_exempt
def train_model(request):
    if request.method == 'POST':
        dataset = request.FILES.get('file')
        username = request.POST['username']
        user_dir = os.path.join(
            'analysis', 'trained-models', f'user_{username}')
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        check = utils.training_models(dataset, username)

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
        model_dir = os.path.join(
            'analysis', 'trained-models', f'user_{username}', model_name)
        df = Testing_models.test_models(dataset, model_dir)
        # write the DataFrame to an Excel file in memory
        excel_file = io.BytesIO()
        with pd.ExcelWriter(excel_file) as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            # create an HttpResponse object with the Excel file as the content
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=my_excel_file.xlsx'
        response.write(excel_file.getvalue())
        return response


@csrf_exempt
def download_file(request, file_path):
    # Get the file name from the file path
    file_name = os.path.basename(file_path)
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Set the response headers
        response = HttpResponse(file.read(
        ), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
