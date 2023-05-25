from django.contrib import admin
from .models import Advertisement,Category,Donation
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id','raiser','title','status','category','created_date','updated_date')

class DonationAdmin(admin.ModelAdmin):
    list_display = ['id' , 'donor' , 'advertisement' , 'amount']
admin.site.register(Advertisement,AdvertisementAdmin)
admin.site.register(Category)
admin.site.register(Donation,DonationAdmin)