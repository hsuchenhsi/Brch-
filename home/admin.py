from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(會員資料)
admin.site.register(會員密碼)
admin.site.register(商品)
admin.site.register(庫存)
admin.site.register(訂單)
admin.site.register(訂單明細)
admin.site.register(購物車)
admin.site.register(評論)
