from django.contrib import admin
from.models import emp

# Register your models here.
class admin_user(admin.ModelAdmin):
    list_display=["id","ename","esalary","eaddress"]
admin.site.register(emp,admin_user)
