from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    return render(request, 'blog/index.html')
