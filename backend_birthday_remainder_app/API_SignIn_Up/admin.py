from django.contrib import admin
from .models import userData
# Register your models here.

# admin.site.register(userData)

@admin.register(userData)
class userDataAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','username','password']