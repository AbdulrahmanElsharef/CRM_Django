from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# ImportExportModelAdmin



@admin.register(End_User)
class End_UserAdmin(admin.ModelAdmin):
    list_display =['name','phone','email','note',]
    list_filter=['name','phone','email']
    
    
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display =['name','logo','note']
    list_filter=['name',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['barcode','des','color','brand','sku','note']
    list_filter=['barcode','brand','color','sku']
    
    
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display =['name','note']
    
@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display =['name','note']
     
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display =['name','note']



class Follow_UpTabularInline(admin.TabularInline):
    model = Follow_Up
class ActionTabularInline(admin.TabularInline):
    model = Action_Detail
    
class IssueTabularInline(admin.TabularInline):
    model = Failer_Detail
class ReportTabularInline(admin.TabularInline):
    model = Report

  
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = [IssueTabularInline,ActionTabularInline,ReportTabularInline,Follow_UpTabularInline]  

    list_display =['__str__','status','client','End_User','Vendor','received_date','note']
    list_filter=['id','status','client','End_User','Vendor__name','received_date',]
    search_fields=('note',)
    


@admin.register(Failer_Detail)
class Failer_DetailAdmin(admin.ModelAdmin):
    list_display =['__str__','product','serial_in','active','invoice','purchase_date','issue','User','company']
    list_filter=["request__id",'product__barcode','serial_in','active','purchase_date','issue__name','request__End_User','request__Vendor__name']
    
    
    
@admin.register(Action_Detail)
class Action_DetailAdmin(admin.ModelAdmin):
    list_display =['__str__','product','serial_out','action','technician','delivery_date','cost',"ref",'User','company',]
    list_filter=["request__id",'product__barcode','serial_out','action__name','technician__name','delivery_date','request__End_User','request__Vendor__name']



@admin.register(Follow_Up)
class Follow_UpAdmin(admin.ModelAdmin):
    list_display =['__str__','connect','msg_kind','comment','rate','note']
    list_filter=['request','connect','msg_kind','rate']


@admin.register(Report)
class Follow_UpAdmin(admin.ModelAdmin):
    list_display =['__str__','complain','Report','advice','note']
    list_filter=['request',]
