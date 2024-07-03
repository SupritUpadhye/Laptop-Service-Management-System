from django.contrib import admin
from .models import User, Customer, ProductInward, Service

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('terms_accepted',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'customerEmail', 'customerMobNo')
    search_fields = ('customerName', 'customerEmail', 'customerMobNo')
    list_filter = ('customerName',)

@admin.register(ProductInward)
class ProductInwardAdmin(admin.ModelAdmin):
    list_display = ('serialNo', 'brand', 'model', 'inwardDate', 'commitmentDate', 'productStatus', 'productChecked', 'customer')
    search_fields = ('serialNo', 'brand', 'model', 'customer__customerName')
    list_filter = ('brand', 'model', 'productStatus', 'productChecked', 'inwardDate', 'commitmentDate')
    date_hierarchy = 'inwardDate'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'component', 'serviceRemark', 'serviceStatus', 'serviceCost', 'product')
    search_fields = ('service_id', 'component', 'serviceRemark', 'serviceStatus', 'product__serialNo')
    list_filter = ('serviceStatus',)
    readonly_fields = ('service_id',)
