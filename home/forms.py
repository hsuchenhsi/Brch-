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
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productNo', 'productName', 'category', 'subcategory', 'describe', 'price', 'picture']
        
class UploadFileForm(forms.Form):
    excel_file = forms.FileField()