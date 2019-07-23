from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})

# Create your views here.

#or
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
