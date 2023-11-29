from urllib import request

from django.http import HttpResponse
from django.shortcuts import render, redirect
from TELECOM.models import customer, ourservices, imagemodel,workers
from TELECOM.forms import ourservicesform, imageuploadform,workersdetailsform
import requests
import json
import base64
from requests.auth import HTTPBasicAuth
from TELECOM.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword

# Create your views here.


def index(request):
    if request.method == 'POST':
        if customer.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            member = customer.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request,'index.html',{'member':customer})
        else:
            return render(request,'login.html')
    else:
        return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        member =customer(firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'],
        username=request.POST['username'],password=request.POST['password'])

        member.save()
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    return  render(request,'login.html')


def inner(request):
    return render(request,'inner-page.html')

def dropdowd():
    return render(request, 'dropdown.html')

def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def add(request):
    if request.method=="POST":
        form = ourservicesform(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/add")
    else:
           form = ourservicesform()
           return render(request, 'addproduct.html', {'form': form})

def show(request):
    product = ourservices.objects.all()
    return render(request,'show.html',{'ourservices': product})

def delete(request ,id):
    product = ourservices.objects.get(id=id)
    product.delete()
    return redirect('/show')

def edit(request, id):
    product = ourservices.objects.get(id=id)
    return render(request,'edit.html',{'ourservices': product})



def update(request, id):
    product = ourservices.objects.get(id=id)
    form = ourservicesform(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'ourservices': product})


def token(request):
    consumer_key = 'f4d7OXZtJgNgmrtOTAvVrOvVDdENwLdz'
    consumer_secret = 'QpQRB36xxAkbsrBN'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r =requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response =requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)


def uploadproducts(request):
    if request.method == 'POST':
        form = imageuploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/uploadproducts')
    else:
        form = imageuploadform()
    return render(request, 'upload products.html', {'form': form})

def showproducts(request):
    images = imagemodel.objects.all()
    return render(request, 'show products.html', {'imagemodel': images})



def workerdelete(request ,id):
    worker = workers.objects.get(id=id)
    worker.delete()
    return redirect('/')

def adddetails(request):
    if request.method == "POST":
        form = workersdetailsform(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/adddetails")
    else:
           form = workersdetailsform()
           return render(request, 'workers details.html', {'form': form})




def showworkersdetails(request):
    worker = workers.objects.all()
    return render(request, 'show workers details.html', {'workers': worker})