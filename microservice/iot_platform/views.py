from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PayloadDevice,PayloadGroup
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


def index(request):
    '''
    views function to rendering home page
    '''
    context = {'title': "TranterIT - IOT - Platform"}
    return render(request, 'index.html',)

def login(request):
    #form = UserCreationForm()
    '''
    views function to rendering login page
    '''
    context = {'title': "login"}
    return render(request, 'login.html',context)
    
#@login_required()
def dash(request):
    '''
    views function to rendering dashboard page
    '''
    context = {'title': "Dashboard - IOT"}
    return render(request, 'dashboard.html',context)

#load all devices from PayloadDevice
def AllPayloadDevice(request):
    thm = PayloadDevice.objects.all().order_by('-added_on')
    context = {'object_list': thm,'title': "All Devices"}
    return render(request, 'pages/Devices.html',context)

def NthPayloadDevice(request,device):
    paydv = get_object_or_404(PayloadDevice, device=device)
    context = {'object': paydv,'title': "Device information"}
    return render(request, 'pages/view_device.html',context)

#add new devices to PayloadDevice
class Client_add_device(View):
    def get(self,request):
        context = {'title': "Add Devices"}
        return render(request, 'pages/add_dev.html',context)
    def post(self,request):
        context = {'title': "Add Devices"}
        return render(request, 'pages/add_dev.html',context)

