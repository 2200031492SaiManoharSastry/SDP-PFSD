from django.contrib import admin

from .models import Admin, register, Contact

# Register your models here.
admin.site.register(Admin)
admin.site.register(register)
admin.site.register(Contact)