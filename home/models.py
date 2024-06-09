from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

from django.shortcuts import render


class MemberData(models.Model):
    memberNo = models.AutoField(primary_key=True, verbose_name='會員編號')
    memberName = models.CharField(max_length=50, verbose_name='會員姓名')
    birthday = models.DateField(verbose_name='生日')
    gender = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')), verbose_name='性別')
    phone = models.CharField(max_length=20, default='', verbose_name='電話')
    email = models.EmailField(max_length=100, verbose_name='電子郵件')
    address = models.CharField(max_length=20, default='', verbose_name='地址')
    password = models.CharField(max_length=100, default='', verbose_name='密碼')

    @property
    def num_str(self):
        return f"M{self.memberNo:04d}"  # 格式化为M0001、M0002等格式
    
    def __str__(self):
        return self.num_str  # 在管理界面中顯示編號不是表單物件

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tops', '上衣'),
        ('bottoms', '下装'),
        ('dresses', '洋装'),
        ('sweaters', '毛衣'),
        ('outerwear', '外套/夾克'),
        ('homewear', '家居'),
        ('shoes', '鞋子'),
        ('bags', '包包'),
        ('accessories', '配件'),
    ]

    SUBCATEGORY_CHOICES = {
        'tops': [
            ('sleeveless', '無袖'),
            ('short_sleeve', '短袖'),
            ('long_sleeve', '長袖'),
            ('shirt', '襯衫'),
        ],
        'bottoms': [
            ('skirts', '裙類'),
            ('shorts', '短褲'),
            ('pants', '長褲'),
            ('jeans', '牛仔褲'),
        ],
        'dresses': [
            ('floral', '小碎花'),
            ('straight', '直筒'),
            ('sleeveless', '無袖'),
        ],
        'sweaters': [
            ('sweater', '毛衣'),
            ('knit_vest', '針織背心'),
            ('knit_cardigan', '針織外套'),
        ],
        'outerwear': [
            ('casual_jacket', '休閒外套'),
            ('windbreaker', '防風外套'),
            ('down_jacket', '羽絨外套'),
            ('coat', '大衣'),
        ],
        'homewear': [
            ('pajamas', '睡衣'),
            ('robe', '睡袍'),
        ],
        'shoes': [
            ('flats', '平底鞋'),
            ('dad_sneakers', '老爹鞋'),
            ('clogs', '洞洞鞋'),
        ],
        'bags': [
            ('handbag', '手提包'),
            ('backpack', '後背包'),
            ('shoulder_bag', '肩背包'),
            ('wallet', '皮夾'),
        ],
        'accessories': [
            ('jewelry', '飾品'),
            ('belt', '皮帶'),
            ('hat', '帽子'),
        ],
    }

    productNo = models.AutoField(primary_key=True,  verbose_name='商品編號')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tops', verbose_name='商品類別')
    subcategory = models.CharField(max_length=50, default='sleeveless', verbose_name='商品子類別')
    productName = models.CharField(max_length=100, verbose_name='商品名稱')
    describe = models.TextField(verbose_name='商品描述')
    picture = models.URLField(verbose_name='圖片')
    price = models.PositiveIntegerField(default=0, verbose_name='價格')

    @property
    def num_str(self):
        return f"P{self.productNo:04d}" 
    
    def __str__(self):
        return f"{self.num_str} - {self.productName}"



    def save(self, *args, **kwargs):
        self.subcategory = dict(self.__class__.SUBCATEGORY_CHOICES[self.category]).get(self.subcategory, self.subcategory)
        super(Product, self).save(*args, **kwargs)

class Store(models.Model):
    storeNo = models.AutoField(primary_key=True, verbose_name='庫存編號')
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品編號')
    size = models.CharField(max_length=2, choices=(('XS', 'XS'),('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'),('F','F')), default='S', verbose_name='尺寸')
    quantity = models.PositiveIntegerField(verbose_name='數量')



    def __str__(self):
        return str(self.storeNo)
                   
class Order(models.Model):
    orderNo = models.AutoField(primary_key=True, verbose_name='訂單編號')
    menberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE, verbose_name='會員編號')
    orderdate = models.DateField(auto_now_add=True, verbose_name='訂單日期')
    pay = models.CharField(max_length=10, choices=(('信用卡', '信用卡'), ('貨到付款', '貨到付款'), ('轉帳', '轉帳')), verbose_name='付款方式')
    total = models.PositiveIntegerField(verbose_name='總金額')
    orderStatus = models.CharField(default='已接受訂單', max_length=5, editable=False, verbose_name='訂單狀態')
    address = models.CharField(max_length=100, verbose_name='寄送地址')
    
  
    def num_str(self):
        today = datetime.today()
        date_str = today.strftime("%Y%m%d")
        return f"{date_str}{self.orderNo:03d}"
    
    def __str__(self):
        return self.num_str()

class OrderDetail(models.Model):
    orderdetailNo = models.AutoField(primary_key=True, verbose_name='訂單明細編號')
    orderNo = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='訂單編號')
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品編號')
    size = models.CharField(max_length=2, choices=(('XS','XS'),('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'),('F','F')), verbose_name='尺寸')
    quantity= models.PositiveIntegerField(verbose_name='數量')
    singlePrice = models.PositiveIntegerField(verbose_name='單價')

    def __str__(self):
        return str(self.orderdetailNo)

class ShopingCart(models.Model):
    shopingcartNo = models.AutoField(primary_key=True, verbose_name='購物車編號')
    menberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE, verbose_name='會員編號')
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品編號')
    size = models.CharField(max_length=2, choices=(('XS','XS'),('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'),('F','F')), verbose_name='尺寸')
    quantity = models.PositiveIntegerField(verbose_name='數量')
    productName = models.CharField(max_length=100, verbose_name='商品名稱', blank=True, null=True)
    picture = models.URLField(verbose_name='圖片', blank=True, null=True)
    price = models.PositiveIntegerField(default=0, verbose_name='價格')


    def __str__(self):
        return str(self.shopingcartNo)
    
    def save(self, *args, **kwargs):
        # 在保存購物車項目時，更新商品名稱、圖片和價格
        Product = self.productNo
        self.productName = Product.productName
        self.picture = Product.picture
        self.price = Product.price
        super().save(*args, **kwargs)

    def cart(request):
        shopping_cart_items = ShopingCart.objects.all()
        for item in shopping_cart_items:
            item.total_price = item.quantity * item.productNo.price
        return render(request, 'cart.html', {'shopping_cart_items': shopping_cart_items})

                   
class Comment(models.Model):
    commentNo = models.AutoField(primary_key=True, verbose_name='評論編號')
    memberNo = models.ForeignKey(MemberData, on_delete=models.CASCADE, verbose_name='會員編號')
    orderNo = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='訂單編號')
    productNo = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品編號')
    score = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='評分')
    message = models.TextField(verbose_name='評論內容')
    commentDate = models.DateField(auto_now_add=True, verbose_name='評論日期')

    def __str__(self):
        return str(self.commentNo)

class Post(models.Model):
    username = models.CharField(max_length=100, verbose_name='用戶名稱')
    email = models.EmailField(verbose_name='電子郵件')
    password = models.CharField(max_length=100, verbose_name='密碼')

    def __str__(self):
        return self.userName
