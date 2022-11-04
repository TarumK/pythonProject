from django.contrib import admin
from .models import Company, Product, Person
    # , Town
# Register your models here.

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Person)
# admin.site.register(Town)