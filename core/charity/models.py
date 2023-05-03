from django.db import models
from accounts.models import User
# Create your models here.
class Advertisement(models.Model):
    '''
    this is a class for define advertisement for charity app
    '''
    raiser = models.ForeignKey('accounts.Profile', on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='ads/'  , default = 'blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL,null = True)

    estimated_amount = models.FloatField()
    collected_amount = models.FloatField(null=True , blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('donor', 'advertisement')