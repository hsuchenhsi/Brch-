from django.contrib import admin 
from .models import *

admin.site.register(MemberData)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(ShopingCart)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
admin.site.register(Post,PostAdmin)

