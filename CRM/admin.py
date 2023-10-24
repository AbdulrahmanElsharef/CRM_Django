from django.contrib import admin
from .models import *

# registerr your models here.
admin.site.register(Brand)
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display =['name','phone','email']
    list_filter=['name','phone','email']
    search_fields=['name',]
admin.site.register(Company)
admin.site.register(Issue)
admin.site.register(Action)
admin.site.register(Color)

class Follow_UpTabularInline(admin.TabularInline):
    model = Follow_Up
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [Follow_UpTabularInline,]
    list_display =['__str__','status','barcode','serial','des','client','company','active','invoice','purchase_date','issue','received_date','action','cost','delivery_date']
    list_filter=['id','status','color','brand','client','company','active','purchase_date','issue','received_date','action','delivery_date']
    search_fields=['barcode','serial']
    # exclude = ('id',)
class Follow_UpAdmin(admin.ModelAdmin):
    list_display =['__str__','connect','comment']
    list_filter=['order','connect','comment']
    search_fields=['comment',]
admin.site.register(Follow_Up,Follow_UpAdmin)


