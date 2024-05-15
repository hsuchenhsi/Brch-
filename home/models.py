from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class MemberData(models.Model):
    menberNo= models.AutoField(primary_key=True)
    menberName = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')))
    phone = models.CharField(max_length=20,default='0')
    email = models.EmailField(max_length=100)

    @property
    def num_str(self):
        return f"M{self.pk:04d}"  # 格式化为M0001、M0002等格式
    
    def __str__(self):
        return self.num_str  # 在管理界面中顯示編號不是表單物件



class MemberPassword(models.Model):
    menberNo = models.OneToOneField(MemberData, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=30, default='your_default_password')  # 儲存加密後的密碼

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  # 加密密码

    def save(self, *args, **kwargs):
        if not self.pk:  # 如果是新记录
            self.set_password(' ')  # 设置初始密码
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.menberNo)  # 在管理界面中顯示編號不是表單物件
class Product(models.Model):
    productNo = models.AutoField(primary_key=True)
    classification = models.CharField(max_length=50)
    productName = models.CharField(max_length=100)
    describe = models.TextField()
    picture = models.CharField(max_length=255)
    price= models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.productNo)
    
class Store(models.Model):
    storeNo = models.AutoField(primary_key=True)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')), default='S')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.storeNo)
                   
class Order (models.Model):
    orderNo = models.AutoField(primary_key=True)
    menberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE)
    orderdate = models.DateField()
    pay = models.CharField(max_length=10, choices=(('信用卡', '信用卡'), ('貨到付款', '貨到付款'), ('轉帳', '轉帳')))
    total = models.PositiveIntegerField()
    orderStatus= models.CharField(max_length=10, choices=(('已接受訂單', '已接受訂單'), ('包貨中', '包貨中'), ('出貨中', '出貨中'), ('物流中心', '物流中心')))
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.orderNo)

class OrderDetail(models.Model):
    orderdetailNo = models.AutoField(primary_key=True)
    orderNo = models.ForeignKey(Order, on_delete=models.CASCADE)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')))
    quantity= models.PositiveIntegerField()
    singlePrice = models.PositiveIntegerField()

    def __str__(self):
        return str(self.orderdetailNo)

class ShopingCart (models.Model):
    shopingcartNo = models.AutoField(primary_key=True)
    menberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE)
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')))
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
    commentDate = models.DateField()

    def __str__(self):
        return str(self.commentNo)
    
