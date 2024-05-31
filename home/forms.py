from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields= {
			'username',
			'email',
			'password'
		}
            
from django import forms
from .models import Product, Store

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productNo', 'productName', 'category', 'subcategory', 'describe', 'price', 'picture']
        
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['productNo', 'size', 'quantity']
        
class UploadFileForm(forms.Form):
    excel_file = forms.FileField()