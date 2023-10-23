from django.db import models
from django.utils import timezone

# Create your models here.
class Brand (models.Model):
    name=models.CharField(("Name"), max_length=25,unique=True)
    image=models.ImageField(("Image"), upload_to='brands',null=True,blank=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    
    def __str__(self):
        return self.name
    
class Client(models.Model):
    name=models.CharField(("Name"), max_length=50)
    phone=models.CharField(("Phone"), max_length=50,unique=True)
    email=models.EmailField(("Email"), max_length=254)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    
    def __str__(self):
        return self.name

ORDER_STATUS=(('Pending','Pending'),('Done','Done'),('Delivered','Delivered'))
WARRANTY=(('In_Active','In_Active'),('Out_Active','Out_Active'))
CONNECT=(('Phone','Phone'),('WatsApp','WatsApp'),('Messenger','Messenger'))
RATE=(('راضى','راضى'),('غير_راضى','غير_راضى'),('يحتاج_تطوير','يحتاج_تطوير'))


class Company(models.Model)  :
    name=models.CharField(("Name"), max_length=250,unique=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    def __str__(self):
        return self.name
    
class Issue(models.Model)  :
    name=models.CharField(("Name"), max_length=25,unique=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    def __str__(self):
        return self.name

class Color(models.Model)  :
    name=models.CharField(("Name"), max_length=25,unique=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    def __str__(self):
        return self.name

class Action(models.Model)  :
    name=models.CharField(("Name"), max_length=25,unique=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    def __str__(self):
        return self.name
    
class Order(models.Model):
    date=models.DateField(("Date"), auto_now=True,)
    status=models.CharField(("Status"), max_length=50,choices=ORDER_STATUS,default=ORDER_STATUS[0])
    barcode=models.CharField(("Barcode"), max_length=50)
    serial=models.CharField(("S.N"), max_length=50,unique=True)
    des=models.CharField(("Description"), max_length=200)
    color=models.ForeignKey(Color, on_delete=models.PROTECT,verbose_name='Color',related_name='order_color')
    brand=models.ForeignKey(Brand, on_delete=models.PROTECT,verbose_name='Brand',related_name='order_brand')
    client = models.ForeignKey(Client, on_delete=models.PROTECT,verbose_name='Client',related_name='order_client')
    active=models.CharField(("Active"), max_length=50,choices=WARRANTY,default=WARRANTY[0])
    company = models.ForeignKey(Company, on_delete=models.PROTECT,verbose_name='Company',related_name='order_Company')
    invoice=models.ImageField(("invoice"), upload_to='Invoice',null=True,blank=True)
    purchase_date=models.DateField(("Purchase_Date"),null=True,blank=True)
    issue=models.ForeignKey(Issue, on_delete=models.PROTECT,verbose_name='Issue',related_name='order_Issue')
    iss_detail=models.TextField(("Detail"),max_length=300,default='Write Issue Detail')
    received_date=models.DateField(("Received_Date"),default=timezone.now)
    action=models.ForeignKey(Action, on_delete=models.PROTECT,verbose_name='Action',related_name='order_Action')
    act_detail=models.TextField(("Detail"),max_length=300,default='Write Action Detail')
    delivery_date=models.DateField(("Delivery_Date"),null=True,blank=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    def __str__(self):
        return f"order--{self.id}"
    
class Follow_Up(models.Model):
    order=models.ForeignKey(Order, on_delete=models.PROTECT,verbose_name='Order',related_name='order_Follow_Up')
    connect=models.CharField(("Connect"), max_length=50,choices=CONNECT,default=ORDER_STATUS[0])
    rate=models.CharField(("Rate"), max_length=50,choices=RATE,default=RATE[0])
    comment=models.TextField(("Comment"),max_length=300,null=True,blank=True)
    note=models.CharField(("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.order)


    