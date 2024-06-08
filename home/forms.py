from django import forms
from .models import Post
from django.contrib.auth.models import User

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

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', '兩次密碼不一致')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)