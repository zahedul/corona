from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from random import randint
from django.http import JsonResponse

@require_http_methods(["GET",])
def index(request):
    data = '0'
    
    return render(request, 'index.html', context={'data': data})

@require_http_methods(["GET",])
def update_status(request):
    data = randint(10, 100)
    
    return JsonResponse({'data': data})