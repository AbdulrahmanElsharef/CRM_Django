from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# ImportExportModelAdmin



@admin.register(End_User)
class End_UserAdmin(admin.ModelAdmin):
    list_display =['name','phone','email','note',]
    list_filter=['name','phone','email']
    search_fields=['name','phone','email']
    
    
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display =['name','logo','note']
    list_filter=['name',]
    search_fields=['name',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['barcode','des','color','brand','sku','note']
    list_filter=['barcode','brand','color','sku']
    search_fields=['barcode','des','color','brand','sku']
    
    
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display =['name','note']
    list_filter=['name',]
    search_fields=['name',]
    
@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display =['name','note']
    list_filter=['name',]
    search_fields=['name',]
     
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display =['name','note']
    list_filter=['name',]
    search_fields=['name',]

class Follow_UpTabularInline(admin.TabularInline):
    model = Follow_Up
class ActionTabularInline(admin.TabularInline):
    model = Action_Detail
class IssueTabularInline(admin.TabularInline):
    model = Failer_Detail
  
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = [IssueTabularInline,ActionTabularInline,]  

    list_display =['__str__','status','client','End_User','Vendor','received_date','delivery_date','ref']
    list_filter=['id','status','client','End_User','Vendor','received_date','delivery_date','ref']
    # search_fields=['__str__','status','client','End_User','Vendor','ref']
    # exclude = ('id',)
    


@admin.register(Failer_Detail)
class Failer_DetailAdmin(admin.ModelAdmin):
    list_display =['__str__','product','serial','active','invoice','purchase_date','issue','User','company','Delivery']
    list_filter=["request__id",'product','serial','active','purchase_date','issue','request__End_User','request__Vendor','request__delivery_date']
    
    # list_filter=['product','serial','active','issue','User','company']

@admin.register(Action_Detail)
class Action_DetailAdmin(admin.ModelAdmin):
    list_display =['__str__','product','serial','action','technician','cost','User','company','Delivery']
    list_filter=["request__id",'product','serial','action','technician','cost','request__End_User','request__Vendor','request__delivery_date']
    # search_fields=["request__id",'product','serial','action','technician',]


@admin.register(Follow_Up)
class Follow_UpAdmin(admin.ModelAdmin):
    list_display =['__str__','connect','msg_kind','comment','rate','note']
    list_filter=['request','connect','msg_kind','rate']
    search_fields=['msg_kind','comment','rate']
