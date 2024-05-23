from import_export import resources, fields
from .models import Product

class ProductResource(resources.ModelResource):
    productNo = fields.Field(attribute='productNo', column_name='id')
    productName = fields.Field(attribute='productName', column_name='name')
    describe = fields.Field(attribute='describe', column_name='description')
    picture = fields.Field(attribute='picture', column_name='photo-src')
    price = fields.Field(attribute='price', column_name='price')

    class Meta:
        model = Product
        import_id_fields = ['productNo']
        # 如果你的 Excel 文件第一行是列名，就可以将 skip_unchanged 设置为 True，以跳过不变的行
        skip_unchanged = True
        report_skipped = False
        skip_rows = 1  # 跳過第一行，即列標題行
    
    def before_import_row(self, row, **kwargs):
    # If 'price' field is empty, mark the row to be skipped
        if not row.get('price'):
            return None
        return super().before_import_row(row, **kwargs)