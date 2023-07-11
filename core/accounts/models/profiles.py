from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to="profile/", default="profile/default_avatar.jpg"
    )
    bank_account_number = models.CharField(
        max_length=16, null=True, blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_complete(self):
        # Add your logic to determine if the profile is complete
        return (
            self.first_name and self.last_name
        )

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
