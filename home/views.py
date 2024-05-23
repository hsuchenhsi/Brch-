from django.shortcuts import render

from home.models import MemberData

# Create your views here.
def frontpage(request):
    return render(request,'frontpage.html')

def login(request):
    return render(request,'login.html')

def A01(request):
    return render(request,'A01.html')

def describe(request):
    return render(request,'describe.html')

def A02(request):
    return render(request,'A02.html')

def order(request):
    return render(request,'order.html')

def describe(request):
    return render(request, 'describe.html')

def information(request):
    try: 
        member = MemberData.objects.get(menberName="test01") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, 'information.html', locals())