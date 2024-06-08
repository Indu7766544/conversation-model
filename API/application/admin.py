from django.contrib import admin

# Register your models here.

from application.models import products

class Product_Admin(admin.ModelAdmin):
      list_display = ['pid','pname','price','company','m_date','E_date']
admin.site.register(products,Product_Admin)