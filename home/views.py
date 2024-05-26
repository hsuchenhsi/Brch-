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


def member(request):
    return render(request, 'member.html')



from django.contrib.auth.hashers import make_password
from .models import CustomUser

def user_login(request):
    if request.method == 'POST':
        # 處理註冊表單的提交
        username = request.POST.get('username')
        email = request.POST.get('email')
        raw_password = request.POST.get('password')
        # 加密密碼
        encrypted_password = make_password(raw_password)
        # 創建用戶對象並保存
        user = CustomUser(username=username, email=email, password=encrypted_password)
        user.save()
        # 渲染註冊成功頁面或其他適當的回應
        return render(request, 'login.html', {'username': username})
    else:
        # GET請求，渲染註冊表單
        return render(request, 'frontpage.html')

