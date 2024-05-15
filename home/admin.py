from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(MemberData)
admin.site.register(MemberPassword)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(ShopingCart)
admin.site.register(Comment)
