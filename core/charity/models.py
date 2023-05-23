from django.db import models
from django.db.models import Sum
from django.urls import reverse
from accounts.models import User
# Create your models here.
class Advertisement(models.Model):
    '''
    this is a class for define advertisement for charity app
    '''
    raiser = models.ForeignKey('accounts.Profile', on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='ads/', default = 'ads/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField(max_length = 2000)
    status = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL , null=True)

    estimated_amount = models.FloatField()
    collected_amount = models.FloatField(default = 0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:144]

    def get_absolute_api_url(self):
        return reverse("charity:api-v1:ads-detail" , kwargs={"pk":self.pk})
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    amount = models.FloatField()
    donated_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('donor', 'advertisement')
    


    
    def save(self, *args, **kwargs):
        self.advertisement.collected_amount += self.amount
        self.advertisement.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.advertisement.title