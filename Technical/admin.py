from django.contrib import admin
from .models import *
# from import_export.admin import ImportExportModelAdmin
# ImportExportModelAdmin


# registerr your models here.
# @admin.register(Brand)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display =['name','logo','note']
#     list_filter=['name',]
#     search_fields=['name',] 

@admin.register(End_User)
class ClientAdmin(admin.ModelAdmin):
    list_display =['name','phone','email','note',]
    list_filter=['name','phone','email']
    search_fields=['name','phone','email']
    
    
@admin.register(Vendor)
class CompanyAdmin(admin.ModelAdmin):
    list_display =['name','logo','note']
    list_filter=['name',]
    search_fields=['name',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['barcode','des','color','brand','sku','note']
    list_filter=['barcode','brand','color','sku']
    search_fields=['barcode','brand','sku']
    
    
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display =['name','note']
    list_filter=['name',]
    search_fields=['name',]
    
@admin.register(Technician)
class ActionAdmin(admin.ModelAdmin):
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
  
class RequestAdmin(admin.ModelAdmin):
    inlines = [IssueTabularInline,ActionTabularInline,Follow_UpTabularInline,]  
admin.site.register(Request,RequestAdmin)

    # list_display =['__str__','status','serial','client','company','received_date','active','purchase','issue','action','cost']
    # list_filter=['id','status','serial','client__name','company','received_date']
    # search_fields=['status','serial','client__name','company__name']
    # exclude = ('id',)
    # def client(self,obj):
    # #     return obj.client__name
    # def active(self,obj):
    #     return obj.order_Failer_Detail.active
    # def invoice(self,obj):
    #     return obj.order_Failer_Detail.invoice
    # def purchase(self,obj):
    #     return obj.order_Failer_Detail.purchase_date
    # def issue(self,obj):
    #     return obj.order_Failer_Detail.issue
    # def action(self,obj):
    #     return obj.order_Action_Detail.action
    # def cost(self,obj):
    #     return obj.order_Action_Detail.cost


admin.site.register(Failer_Detail)
# class Failer_DetailAdmin(admin.ModelAdmin):
    # list_display =['__str__','active','invoice','purchase_date','issue','detail','note']
    # list_filter=['request__id','active','purchase_date','issue__name']
    # search_fields=['issue__name','detail',]
    


admin.site.register(Action_Detail)
# class Action_DetailAdmin(admin.ModelAdmin):
    # list_display =['__str__','action','detail','cost','note']
    # list_filter=['request','action','cost']
    # search_fields=['action','detail']

admin.site.register(Follow_Up)
# class Follow_UpAdmin(admin.ModelAdmin):
    # list_display =['__str__','connect','msg_kind','comment','rate','note']
    # list_filter=['request','connect','msg_kind','rate']
    # search_fields=['msg_kind','comment','rate']
