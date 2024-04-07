from django.shortcuts import render
from .models import user
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import user
import json
# from .forms import UserUpdateForm
# test_value = request.POST.get('test')[:10]

# win_value = request.POST.get('win')
# from django.http import JsonResponse
# import json

@csrf_exempt
def signup(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'This endpoint only supports POST requests.'}, status=405)
    
    try:
        data_body = json.loads(request.body)
        test_value = data_body.get('test')[:10]
        win_value = data_body.get('win')

        # test_value = request.POST.get('test')[:10]
        #
        # win_value = request.POST.get('win')[:10]
        if test_value is None or win_value is None:
            return JsonResponse({'error': 'NULLL'}, status=400)
        
        if user.objects.filter(test=test_value).exists():
            return JsonResponse({'error': 'Username already exists.'})
        
        user.objects.create(test=test_value, win=win_value)
        return JsonResponse({'message': 'User created successfully.'})
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# views.py

# from django.shortcuts import render
# from .models import YourModel
from django.http import JsonResponse
def search_view(request):
    query = request.GET.get('q')
    results = None
    if query:
        # Perform search using Django's ORM
        results = user.objects.filter(test__icontains=query)
        # Extracting the names from the queryset
        results_names = [result.test for result in results]
        return JsonResponse({'results': results_names})
    return JsonResponse({'results': []})


@csrf_exempt   
    # return render(request, 'search_results.html', {'results': results, 'query': query})
def update_user(request, user_id):
    user_instance = get_object_or_404(user, pk=user_id)
    
    if request.method == 'POST':
        # form = UserUpdateForm(request.POST, instance=user_instance)
        if user_instance.test and user.objects.filter(id =user_id).exists():
            user.objects.update(test=request.POST.get('test'))
            # user_instance.test=request.
            return JsonResponse({'message': 'User updated successfully'})
        else:
            return JsonResponse({'error'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
@csrf_exempt 
def delete(request,id):
    if request.method =='POST':
        if user.objects.filter(id = id ).exists():
            objct = user.objects.get(id=id)
            objct.delete()
            return JsonResponse({'message': 'User Delete successfully'})
        else:
                return JsonResponse({'error'}, status=400)
            
    else:
         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
def   display(request):
    # if
    obect = user.objects.order_by('-win')[:3]
    for _ in obect:
      print(_.id , ' id',_.test,' test',_.win,' win_number')
    return JsonResponse({'win_three': 'Display'})
    # pass
 
    