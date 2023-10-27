from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.

ORDER_STATUS=(("",""),('Pending','Pending'),('Done','Done'),('Delivered','Delivered'))
MESSAGE_KIND=(("",""),('Pending_MSG','Pending_MSG'),('Done_MSG','Done_MSG'),('Delivered_MSG','Delivered_MSG'),('FollowUP_MSG','FollowUP_MSG'))
WARRANTY=(("",""),('In_Warranty','In_Warranty'),('Out_Warranty','Out_Warranty'))
CONNECT=(("",""),('Phone','Phone'),('WatsApp','WatsApp'),('Messenger','Messenger'))
RATE=(("",""),('راضى','راضى'),('غير_راضى','غير_راضى'),('يحتاج_تطوير','يحتاج_تطوير'))
CLIENT_kind=(("",""),('End_User','End_User'),('Vendor','Vendor'))


    
class End_User(models.Model):
    name=models.CharField(_("Name"), max_length=50)
    phone=models.CharField(_("Phone"), max_length=25)
    email=models.EmailField(_("Email"), max_length=50,default='user@alt.com')
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "End_User"

class Vendor(models.Model):
    name=models.CharField(_("Name"), max_length=100,unique=True)
    logo=models.ImageField(_("Logo"), upload_to='Vendor',null=True,blank=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "Vendor"
    
    
class Product(models.Model):
    barcode=models.CharField(_("Barcode"), max_length=50,unique=True)
    des=models.CharField(_("Description"), max_length=200)
    color=models.CharField(_("Color"), max_length=50)
    brand=models.CharField(_("Brand"), max_length=50)
    sku=models.CharField(_("Sku"), max_length=50)
    note=models.CharField(_("Note"), max_length=50,default='No Note')

    def __str__(self):
        return str(self.barcode)
    
    
    
class Issue(models.Model)  :
    name=models.CharField(_("Name"), max_length=25,unique=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)

class Technician(models.Model)  :
    name=models.CharField(_("Name"), max_length=25,unique=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)

class Action(models.Model)  :
    name=models.CharField(_("Name"), max_length=25,unique=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)

    
class Request(models.Model):
    status=models.CharField(_("Status"), max_length=50,choices=ORDER_STATUS,default=ORDER_STATUS[0])
    client=models.CharField(_("client"), max_length=50,choices=CLIENT_kind,default=ORDER_STATUS[0])
    End_User = models.ForeignKey(End_User, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Client'),related_name='Request_client')
    Vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT,verbose_name=_('Vendor'),related_name='Request_Vendor')
    received_date=models.DateField(_("Received_Date"),default=timezone.now)
    delivery_date=models.DateField(_("Delivery_Date"),null=True,blank=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return f"REQ--{str(self.id)}"
    
        
class Failer_Detail(models.Model)  :
    request=models.ForeignKey(Request, on_delete=models.PROTECT,verbose_name=_('Request'),related_name='request_Failer_Detail')
    product=models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name=_('Product'),related_name='Failer_Detail_Product')
    serial=models.CharField(_("S.N"), max_length=50)
    active=models.CharField(_("Active"), max_length=25,choices=WARRANTY,default=WARRANTY[0])
    invoice=models.ImageField(_("invoice"), upload_to='Invoice',null=True,blank=True)
    purchase_date=models.DateField(_("Purchase_Date"),null=True,blank=True)
    issue=models.ForeignKey(Issue, on_delete=models.PROTECT,verbose_name='Issue',related_name='Issue_name')
    detail=models.CharField(_("Detail"),max_length=300,default='Write Issue Detail')
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    
    def __str__(self):
        return str(self.request)
    
class Action_Detail(models.Model)  :
    request=models.ForeignKey(Request, on_delete=models.PROTECT,verbose_name=_('Request'),related_name='request_Action_Detail')
    product=models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name=_('Product'),related_name='Action_Detail_Product')
    serial=models.CharField(_("S.N"), max_length=50)
    action=models.ForeignKey(Action, on_delete=models.PROTECT,verbose_name='Action',related_name='Action_name')
    detail=models.CharField(_("Detail"),max_length=300,default='Write Action Detail')
    technician=models.ForeignKey(Technician, on_delete=models.PROTECT,verbose_name='Technician',related_name='Action_Technician')
    cost=models.IntegerField(_("Cost"),default=0)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.request)
    
class Follow_Up(models.Model):
    request=models.ForeignKey(Request, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Request'),related_name='request_Follow_Up')
    connect=models.CharField(_("Connect"), max_length=50,choices=CONNECT,default=ORDER_STATUS[0])
    msg_kind=models.CharField(_("Message"), max_length=50,choices=MESSAGE_KIND,default=RATE[0])
    comment=models.TextField(_("Comment"),max_length=500,null=True,blank=True)
    rate=models.CharField(_("Rate"), max_length=50,choices=RATE,default=RATE[0])
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.request)

    class Meta:
        verbose_name_plural = "Follow_Up"
    
