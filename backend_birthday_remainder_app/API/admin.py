from django.contrib import admin
from .models import remainderData

# @admin.register(remainderData)
# class remainderDataAdmin(admin.ModelAdmin):
#     list_display = ['id','name','date','quota','photoName']


admin.site.register(remainderData)