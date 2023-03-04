from django.shortcuts import render
from django.http import HttpResponse
from .prediction import start_chat , chatbot_response
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def sayhello(request):
#     return HttpResponse('Hello Django')

# def chat_response(request):
#     chat_responses =  start_chat()
#     return HttpResponse(chat_responses)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


# def process_question(request):
#     # Extract the question from the request body
#     question = request.POST.get('question')

#     # Process the question and generate a response
#     answer = chatbot_response(question)
#     response = {'answer': answer}

#     # Send the JSON response back to the frontend
#     return JsonResponse(response)

@csrf_exempt
def chat_responses(request):
    print(request)
    if request.method == 'POST':
        json_data = json.loads(request.body)
        question = json_data['question']
        # question = request.POST.get('question')
        print(question)
        chat_responses = start_chat(str(question))
        response_data = {'response': chat_responses}
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        return HttpResponse(status=405)
    