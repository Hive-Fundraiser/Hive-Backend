from django.test import TestCase
from datetime import datetime

from ..models import Advertisement, Category
from accounts.models import User,Profile

class TestAdvertisementModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com",password="a/@1234567")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name = "test_first_name",
            last_name = "test_last_name",
        )

    def test_create_post_with_valid_data(self):
        
        post = Advertisement.objects.create(
            raiser = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = None,
            estimated_amount = 0,
            published_date = "2023-06-13T20:39:46.744Z"
        )
        self.assertTrue(Advertisement.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title,"test")
