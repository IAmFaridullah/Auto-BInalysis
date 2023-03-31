from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from analysis import utils
import os
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from fpdf import FPDF

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
        

def test_model(request):
    if request.method == 'POST':
        dataset = request.FILES.get('file')
        username = request.POST['username']
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

        pdf = FPDF()
        header = list(df.columns)
        cell_width = 40
        cell_height = 10
        
        # Create the PDF table
        pdf.set_font("Arial", "B", 12)
        for col in header:
            pdf.cell(cell_width, cell_height, col, border=1)
        pdf.ln()

        pdf.set_font("Arial", "", 12)
        for index, row in df.iterrows():
            for col in header:
                # Use MultiCell instead of Cell to wrap text
                pdf.cell(cell_width, cell_height,
                         str(row[col]), border=1)
            pdf.ln()

        # Save the PDF
        pdf_bytes = pdf.output(dest='S')
        # convert the bytearray to a string
        pdf_str = pdf_bytes.decode('latin-1')
        pdf_encoded = pdf_str.encode('latin-1')

    # Create a response with the PDF as content
        response = FileResponse(pdf_encoded, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="dataframe.pdf"'
    # Send the response to the client
        return response

        # return HttpResponse("File uploaded successfully.", status=200)
    return HttpResponse("Server is expecting post request for dataset upload", status=400)
