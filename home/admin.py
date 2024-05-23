from django.contrib import admin


from .models import *
from import_export.admin import ImportExportModelAdmin
from .models import Product
from .resources import ProductResource

##pip install django-import-export 先下載
##pip install openpyxl 用於處理 Excel 檔案
admin.site.register(MemberData)

admin.site.register(Store)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(ShopingCart)
admin.site.register(Comment)

from import_export.formats import base_formats
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    formats = (base_formats.XLSX,) 
    import_id_fields = ['id']#主鍵
    import_fields = ['name', 'price', 'photo-src', 'description']
    skip_unchanged = True  # 跳过未更改的行
    report_skipped = False  # 不报告跳过的行
admin.site.register(Product, ProductAdmin)
