from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request,'frontpage.html')

def login(request):
    return render(request,'login.html')

def A01(request):
    return render(request,'A01.html')

def A02(request):
    return render(request,'A02.html')