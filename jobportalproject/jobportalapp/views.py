

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from . models import *


def index(request):
     return render(request,'mainindex.html')
def mainindex(request):
     return render(request,'mainindex.html') 
def user_login(request):
     return render(request,'userlogin.html') 
def user_register(request):
     return render(request,'Register/userregister.html') 