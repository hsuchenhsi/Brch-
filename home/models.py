from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class MemberData(models.Model):
    memberNo = models.AutoField(primary_key=True)
    memberName = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')))
    phone = models.CharField(max_length=20,default='0')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,default=0)

    @property
    def num_str(self):
        return f"M{self.memberNo:04d}"  # 格式化为M0001、M0002等格式
    
    def __str__(self):
        return self.num_str  # 在管理界面中顯示編號不是表單物件

class Product(models.Model):
    productNo = models.CharField(primary_key=True, max_length=10)
    productName = models.CharField(max_length=100)
    describe = models.TextField()
    picture = models.URLField()
    price= models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.productNo)
    
class Store(models.Model):
    storeNo = models.AutoField(primary_key=True)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')), default='S')
    quantity = models.PositiveIntegerField()

    def num_str(self):
        return f"s{self.storeNo:04d}" 
    
    def __str__(self):
        return str(self.storeNo)
                   
class Order(models.Model):
    orderNo = models.AutoField(primary_key=True)
    menberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE)
    orderdate = models.DateField(auto_now_add=True)
    pay = models.CharField(max_length=10, choices=(('信用卡', '信用卡'), ('貨到付款', '貨到付款'), ('轉帳', '轉帳')))
    total = models.PositiveIntegerField()
    orderStatus = models.CharField(default='已接受訂單', max_length=5, editable=False)
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.orderNo)
    
    def num_str(self):
        today = datetime.today()
        date_str = today.strftime("%Y%m%d")
        return f"{date_str}{self.orderNo:03d}"

class OrderDetail(models.Model):
    orderdetailNo = models.AutoField(primary_key=True)
    orderNo = models.ForeignKey(Order, on_delete=models.CASCADE)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=(('XS','XS'),('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')))
    quantity= models.PositiveIntegerField()
    singlePrice = models.PositiveIntegerField()

    def __str__(self):
        return str(self.orderdetailNo)

class ShopingCart(models.Model):
    shopingcartNo = models.AutoField(primary_key=True)
    menberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, choices=(('XS','XS'),('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')))
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.shopingcartNo)
                   
class Comment(models.Model):
    commentNo = models.AutoField(primary_key=True)
    memberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE)
    orderNo = models.ForeignKey(Order, on_delete=models.CASCADE)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    message = models.TextField()
    commentDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.commentNo)
