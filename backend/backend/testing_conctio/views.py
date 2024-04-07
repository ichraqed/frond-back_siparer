from django.shortcuts import render
from user_interface.models import user
from django.http import JsonResponse
# Create your views here.
def test(request,id):
    object = user.objects.get(id=id)
    if object:
        object.win=object.win+1
        object.save()
    return JsonResponse({'add':'add_win'})