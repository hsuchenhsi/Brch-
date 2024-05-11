from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


from django.db.models import F

class 會員資料(models.Model):
    會員編號= models.AutoField(primary_key=True)
    姓名 = models.CharField(max_length=50)
    生日 = models.DateField()
    性別 = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')))
    電話號碼 = models.CharField(max_length=20)
    電子郵件 = models.EmailField(max_length=100)

    @property
    def num_str(self):
        return f"M{self.pk:04d}"  # 格式化为M0001、M0002等格式

    def __str__(self):
        return self.num_str  # 在管理界面中顯示編號不是表單物件



class 會員密碼(models.Model):
    會員編號 = models.OneToOneField(會員資料, on_delete=models.CASCADE, primary_key=True)
    密碼 = models.CharField(max_length=128, default='your_default_password')  # 儲存加密後的密碼

    def set_password(self, raw_password):
        self.密碼 = make_password(raw_password)  # 加密密码

    def save(self, *args, **kwargs):
        if not self.pk:  # 如果是新记录
            self.set_password(' ')  # 设置初始密码
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.會員編號)  # 在管理界面中顯示編號不是表單物件
class 商品(models.Model):
    商品編號 = models.AutoField(primary_key=True)
    分類 = models.CharField(max_length=50)
    名稱 = models.CharField(max_length=100)
    商品介紹 = models.TextField()
    圖片 = models.CharField(max_length=255)
    價格= models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.商品編號)
    
class 庫存(models.Model):
    庫存編號 = models.AutoField(primary_key=True)
    商品編號 = models.ForeignKey(商品, on_delete=models.CASCADE)
    尺寸 = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')), default='S')
    數量 = models.PositiveIntegerField()

    def __str__(self):
        return str(self.庫存編號)
                   
class 訂單(models.Model):
    訂單編號 = models.AutoField(primary_key=True)
    會員編號 = models.ForeignKey(會員資料, on_delete=models.CASCADE)
    下單日期 = models.DateField()
    付款方式 = models.CharField(max_length=10, choices=(('信用卡', '信用卡'), ('貨到付款', '貨到付款'), ('轉帳', '轉帳')))
    金額 = models.PositiveIntegerField()
    訂單狀態 = models.CharField(max_length=10, choices=(('已接受訂單', '已接受訂單'), ('包貨中', '包貨中'), ('出貨中', '出貨中'), ('物流中心', '物流中心')))
    送貨地址 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.訂單編號)

class 訂單明細(models.Model):
    訂單明細編號 = models.AutoField(primary_key=True)
    訂單編號 = models.ForeignKey(訂單, on_delete=models.CASCADE)
    商品編號 = models.ForeignKey(商品, on_delete=models.CASCADE)
    尺寸 = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')))
    數量 = models.PositiveIntegerField()
    價錢 = models.PositiveIntegerField()

    def __str__(self):
        return str(self.訂單明細編號)

class 購物車(models.Model):
    購物車編號 = models.AutoField(primary_key=True)
    會員編號 = models.ForeignKey(會員資料, on_delete=models.CASCADE)
    商品編號 = models.ForeignKey(商品, on_delete=models.CASCADE)
    尺寸 = models.CharField(max_length=1, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('F', 'F')))
    數量 = models.PositiveIntegerField()

    def __str__(self):
        return str(self.購物車編號)
                   
class 評論(models.Model):
    評論編號 = models.AutoField(primary_key=True)
    會員編號 = models.ForeignKey(會員資料, on_delete=models.CASCADE)
    訂單編號 = models.ForeignKey(訂單, on_delete=models.CASCADE)
    商品編號 = models.ForeignKey(商品, on_delete=models.CASCADE)
    評分 = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    留言 = models.TextField()
    評分日期 = models.DateField()

    def __str__(self):
        return str(self.評論編號)
    
