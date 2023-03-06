from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def anna(request):
    return HttpResponse('krishna is the brother of ballaraam')

def macha(request):
    return HttpResponse('<marquee><h1>vadule macha</h1></marquee>')