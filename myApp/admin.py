from django.contrib import admin
from .models import *
# Register your models here.

class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place_name', 'comments', 'longitude', 'latitude', 'created_at')
    readonly_fields = ('id',)

admin.site.register(Memory, MemoryAdmin)
