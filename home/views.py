from django.shortcuts import render,get_object_or_404

from home.models import MemberData,Product,Store

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

def information(request):
    try: 
        member = MemberData.objects.get(menberName="test01") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, 'information.html', locals())


def member(request):
    return render(request, 'member.html')



from django.contrib.auth.hashers import make_password
from .models import Post

def user_login(request):
    if request.method == 'POST':
        # 處理註冊表單的提交
        username = request.POST.get('username')
        email = request.POST.get('email')
        raw_password = request.POST.get('password')
        # 加密密碼
        encrypted_password = make_password(raw_password)
        # 創建用戶對象並保存
        user = Post(username=username, email=email, password=encrypted_password)
        user.save()
        # 渲染註冊成功頁面或其他適當的回應
        return render(request, 'login.html', {'username': username})
    else:
        # GET請求，渲染註冊表單
        return render(request, 'frontpage.html')

from django.shortcuts import render, redirect
from .forms import ProductForm,StoreForm
from django.contrib import messages
def manage_products(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        store_form = StoreForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, '新增商品成功！')
            return redirect('manage_products')
    else:
        product_form = ProductForm()
        store_form = StoreForm()


    products = Product.objects.all()
    stores = Store.objects.all()
    return render(request, 'manage_products.html', {
        'product_form': product_form,
        'store_form': store_form,
        'products': products,
        'stores': stores
    })

def delete_product(request, productNo):
    product = get_object_or_404(Product, productNo=productNo)
    if request.method == 'POST':
        product.delete()
        return redirect('manage_products')
    return render(request, 'delete_product.html', {'product': product})

def edit_product(request, productNo):
    product = get_object_or_404(Product, productNo=productNo)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})


from django.conf import settings
from .forms import UploadFileForm

from import_export.fields import Field 
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        # 处理您的 Excel 文件并将数据保存到数据库
        # 这里假设您使用了 pandas 来处理 Excel 文件
        import pandas as pd
        df = pd.read_excel(excel_file)
        for index, row in df.iterrows():
            if pd.isna(row['category']) or pd.isna(row['subcategory']) or pd.isna(row['name']) or pd.isna(row['description']) or pd.isna(row['photo-src']) or pd.isna(row['price']):
                # 如果有空值或nan值，跳过这一行
                continue
            #Excel讀取的資料
            Product.objects.create(
                category=row['category'],
                subcategory=row['subcategory'],
                productName=row['name'],
                describe=row['description'],
                picture=row['photo-src'],
                price=row['price']
            )
        return HttpResponse('上傳成功')
    return render(request, 'upload.html')

def manage_store(request):
    if request.method == 'POST':
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            store_form.save()
            messages.success(request, '新增庫存成功！')
            return redirect('manage_store')
    else:
        store_form = StoreForm()

    stores = Store.objects.all()
    return render(request, 'manage_store.html', {
        'store_form': store_form,
        'stores': stores
    })

def delete_store(request, storeNo):
    store = get_object_or_404(Store, storeNo=storeNo)
    if request.method == 'POST':
        store.delete()
        messages.success(request, '庫存已刪除！')
        return redirect('manage_store')
    return render(request, 'delete_store.html', {'store': store})

def edit_store(request, storeNo):
    store = get_object_or_404(Store, storeNo=storeNo)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('manage_store')
    else:
        form = StoreForm(instance=store)

    return render(request, 'edit_store.html', {'store_form': form})