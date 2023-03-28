import pandas as pd
from django.http import HttpResponse, JsonResponse
from .prediction import start_chat
import json
import os
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from userauthentication.models import client_details
from .models import Chat, Admin
from django.contrib.contenttypes.models import ContentType
from fpdf import FPDF


def get_chats(request):
    chat_users = client_details.objects.filter(
        chat__isnull=False).distinct()
    users_data = [{'username': user.username, 'name': user.account_name,
                   'email': user.email} for user in chat_users]
    return JsonResponse({'users': users_data}, status=200)


@csrf_exempt
def get_user_chats(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']
        if username:
            user_chats = Chat.objects.filter(
                sender__username=username)
            chats = [{'message': chat.message, 'isSender': 'true'}
                     for chat in user_chats]
            return JsonResponse({'user_chats': chats}, status=200)
        else:
            return JsonResponse({'message': 'username was not provided.'}, status=404)


@csrf_exempt
def admin_message(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        message = json_data['message']
        if message:
            user = client_details.objects.get(username='iamelliot')
            admin = Admin.objects.get(Username='iamadmin')
            sender_type = ContentType.objects.get_for_model(admin)
            receiver_type = ContentType.objects.get_for_model(user)
            chat = Chat.objects.create(message=message, sender_type=sender_type,
                                       reciever_type=receiver_type, msg_time=timezone.now())
            chat.save()
        else:
            return JsonResponse({'message': 'no message was provided.'})


@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        question = json_data['question']
        chat_response = start_chat(str(question))
        if chat_response == 'Transferring the request to admin':
            user = client_details.objects.get(username='iamelliot')
            admin = Admin.objects.get(Username='iamadmin')
            new_chat = Chat(sender=user, reciever=admin, message=question,
                            msg_time=timezone.now())
            new_chat.save()

        response_data = {'answer': chat_response}
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        return HttpResponse(status=405)


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

#         pdf = FPDF()

#         pdf.add_page()

# # Set the font and font size for the PDF
#         pdf.set_font("Arial", size=12)

# # Write the dataframe to the PDF
#         for col in df.columns:
#             pdf.cell(0, 10, col, ln=1)

# # Save the PDF
#         pdf.output("dataframe.pdf")
#         # PDF

        return HttpResponse("File uploaded successfully.", status=200)
    return HttpResponse("Server is expecting post request for dataset upload", status=400)
