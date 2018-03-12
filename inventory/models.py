from django.db import models

# Create your models here.

# 厂商信息
class Provider(models.Model):
    # Id
    name = models.CharField(max_length=10, default="") # 厂商名
    tel = models.CharField(max_length=20, default="") # 联系电话

    def __str__(self):
        return self.name


# 产品信息
class Product(models.Model):
    # A primary key field will automatically be added to your model
    # Id
    original_id = models.CharField(max_length=10, default="") # 原产品编号
    current_id = models.CharField(max_length=10, default="") # 现产品编号
    name = models.CharField(max_length=10, default="") # 名称
    material = models.CharField(max_length=10, default="") # 面料
    color = models.CharField(max_length=10, default="") # 颜色
    size = models.CharField(max_length=10, default="") # 尺码
    unit = models.CharField(max_length=10, default="") # 单位
    unit_price = models.IntegerField(default=0) # 单价
    cost = models.IntegerField(default=0) # 成本
    default_price = models.IntegerField(default=0) # 售价
    remarks  = models.CharField(max_length=256, default="") # 备注
    price_coff = models.FloatField(default=1) # 定价系数

    def __str__(self):
        return self.name

                            
# 进货单
class Purchase(models.Model):
    # Id
    purchase_id = models.CharField(max_length=10, default="") # 进货单编号
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # 产品编号
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE) # 厂商编号
    number= models.IntegerField(default=0) # 入库数量
    purchase_date = models.DateTimeField('date purchased') # 入库日期

    def __str__(self):
        return self.purchase_id
