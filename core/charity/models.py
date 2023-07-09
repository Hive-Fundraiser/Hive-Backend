from django.db import models
from django.db.models import Sum
from django.urls import reverse
from accounts.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Advertisement(models.Model):
    """
    this is a class for define advertisement for charity app
    """

    raiser = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="ads/", default="ads/default.jpg")
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=700)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )

    estimated_amount = models.FloatField()
    collected_amount = models.FloatField(default=0)

    @property
    def collected_percentage(self):
        if self.estimated_amount == 0:
            return 0
        return round((self.collected_amount / self.estimated_amount), 2) * 100

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def clean(self):
        super().clean()

        if self.estimated_amount < 0:
            raise ValidationError("مقدار نمی تواند منفی باشد")

        if self.collected_amount < 0:
            raise ValidationError("مبلغ جمع آوری شده نمی تواند منفی باشد.")
        
        if len(self.title) > 255:
            raise ValidationError("موضوع نمی تواند بیشتر از 255 کاراکتر باشد")

        if len(self.content) > 700:
            raise ValidationError("متن نمی تواند بیشتر از 500 کاراکتر باشد")
        
    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:144]

    def get_absolute_api_url(self):
        return reverse("charity:api-v1:ads-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Donation(models.Model):
    donor = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    amount = models.FloatField()
    donated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.advertisement.collected_amount += self.amount
        self.advertisement.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.advertisement.title

    def clean(self):
        super().clean()

        if self.collected_amount >= self.estimated_amount:
            self.status = False 
            
        if self.amount < 0:
            raise ValidationError("مقدار نمی تواند منفی باشد")

        if self.amount > self.advertisement.estimated_amount:
            raise ValidationError("مبلغ نمی تواند بیشتر از میزان اعتبار باشد")

        if self.amount > (self.advertisement.estimated_amount - self.advertisement.collected_amount):
            raise ValidationError("مبلغ نمی تواند از مقدار جمع آوری شده بیشتر باشد")

    def __str__(self):
        return self.advertisement.title