from django.shortcuts import render
from .views import *
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.
def Sign_up(request):
    if request.method != 'POST':
        data_body = json.loads(request)
        fullName  = data_body.get('fullName')
        gender =  data_body.get('gender')
        status = data_body.get('status')
        email = data_body.get('email')
        username = data_body.get('username')
        passwordHash = data_body.get('passwordHash')
        if User.objects.filter(username=username).exists()  or user.objects.filter(email=email).exists(): 
            # rederecter Signup
           return JsonResponse({'success': False, 'message': 'Username or email already exists'})
        user = User.objects.create(username=username,fullName=fullName,email=email,gender=gender,status=status)
        user.set_password(passwordHash)
        user.save()
        return JsonResponse({'success': True, 'message': 'Signup successful'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})