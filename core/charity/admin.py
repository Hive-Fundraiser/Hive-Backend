from django.contrib import admin
from .models import Advertisement,Category
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('raiser','title','status','category','created_date','updated_date')

admin.site.register(Advertisement,AdvertisementAdmin)
admin.site.register(Category)