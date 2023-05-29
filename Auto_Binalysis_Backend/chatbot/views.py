import pandas as pd
from django.http import HttpResponse, JsonResponse, FileResponse
from .prediction import start_chat
import json
import re
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from userauthentication.models import client_details
from adminpanel.models import Admin
from .models import Chat
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
import uuid


def get_chats(request):
    chat_users = client_details.objects.filter(
        sender_chats__isnull=False, email__isnull=False, is_admin=False).distinct()
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
                Q(sender__username=username) | Q(receiver__username=username)
            ).order_by('msg_time')
            chats = [{'message': chat.message, 'sender': chat.sender_id}
                     for chat in user_chats]

            return JsonResponse({'user_chats': chats}, status=200)
        else:
            return JsonResponse({'message': 'username was not provided.'}, status=404)


@csrf_exempt
def admin_message(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        message = json_data['message']
        username = json_data['username']
        if message:
            admin = client_details.objects.get(username='iamadmin')
            user = client_details.objects.get(username=username)
            chat = Chat(sender=admin, receiver=user,
                        message=message, msg_time=timezone.now())
            chat.save()
            send_mail(
                'Reply from auto-binalysis admin',  # email subject
                'Here is the answer of admin about the query you asked in chatbot.',  # email body
                settings.EMAIL_HOST_USER,  # email from address
                [user.email],  # email recipient list
                html_message='Hi <h4 style="display: inline-block;">{}</h4>,<br>{}<br><br>Thanks,<br>Admin'.format(
                    user.username, message),
                fail_silently=False,  # set to True to ignore errors when sending the email
            )
            return JsonResponse({'message': 'message sent successfully'}, status=200)

        else:
            return JsonResponse({'message': 'no message was provided.'})


@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        question = json_data['question']
        username = None
        user = None
        if json_data.get('username', None):
            username = json_data['username']
            user = client_details.objects.get(username=username)

        chat_response = start_chat(str(question))
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(email_regex, question):
            email = question
            guest_username = json_data['guest_username']
            user = client_details.objects.get(username=guest_username)
            user.email = email
            user.save()
            response_data = {
                'answer': "Thanks for providing your email. Admin will respond to your query shortly."}
        elif chat_response == 'Transferring the request to admin':
            admin = client_details.objects.get(username='iamadmin')
            if user:
                new_chat = Chat(sender=user, receiver=admin,
                                message=question, msg_time=timezone.now())
                new_chat.save()
                chat_response = ""
                response_data = {
                    'answer': "Please wait, admin will respond to your query on your email."}
            else:
                # CREATING GUEST USER
                guest_username = str(uuid.uuid4())[:8]
                name = f"Guest user {client_details.objects.filter(account_name__startswith='Guest user').count() + 1}"
                user = client_details.objects.create(
                    username=guest_username, account_name=name)
                new_chat = Chat(sender=user, receiver=admin,
                                message=question, msg_time=timezone.now())
                new_chat.save()
                response_data = {
                    'answer': "Kindly, send your email so that admin can respond.",
                    'guest_username': user.username}
        else:
            response_data = {
                'answer': chat_response}
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        return HttpResponse(status=405)
