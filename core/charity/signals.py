from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Advertisement
from .exceptions import ImageUploadError


@receiver(pre_save, sender=Advertisement)
def validate_image(sender, instance, **kwargs):
    if instance.image:
        # Check if the image size is too large
        if instance.image.size > 1024 * 1024:
            raise ImageUploadError("Image size must be less than 1 MB")
