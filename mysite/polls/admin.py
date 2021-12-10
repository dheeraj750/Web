from django.contrib import admin
from polls.models import Contact

# Register your models here.
admin.site.register(Contact)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','content']