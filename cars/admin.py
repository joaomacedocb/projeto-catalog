from django.contrib import admin
from cars.models import Brand
from cars.models import Car

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factoryYear','modelYear','value',)
    search_fields = ('model',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)