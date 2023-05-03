from django.shortcuts import render
from django.http import JsonResponse
from userauthentication.models import client_details
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def get_users(request):
    raw_users = client_details.objects.filter(
        email__isnull=False, is_admin=False)
    users = [{'username': user.username, 'name': user.account_name, 'email': user.email, 'city': user.org_city,
              'country': user.org_country} for user in raw_users]
    return JsonResponse({'users': users}, status=200)


@csrf_exempt
def delete_user(request):
    json_data = json.loads(request.body)
    username = json_data['username']
    user = client_details.objects.get(email='elliot@db.com')
    user.delete()
    return JsonResponse({'message': 'User deleted successfully.'}, status=200)


@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        user_data = json_data['userData']
        user = client_details.objects.get(username=user_data['username'])
        user.email = user_data['email']
        user.account_name = user_data['name']
        user.org_city = user_data['city']
        user.org_country = user_data['country']
        user.save()
        return JsonResponse({}, status=200)
