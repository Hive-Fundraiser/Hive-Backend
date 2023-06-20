from django.core.management.base import BaseCommand

from faker import Faker
import random
from datetime import datetime

from accounts.models import User, Profile
from charity.models import Advertisement, Category , Donation


category_list = ["IT", "Design", "Fun"]
num_advertisements = Advertisement.objects.count()

class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            email=self.fake.email(), password="Test@123456")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Advertisement.objects.create(
                raiser=profile,
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=10),
                status=random.choice([True, False]),
                category=Category.objects.get(
                    name=random.choice(category_list)),
                estimated_amount=self.fake.random_number(fix_len=False),
                published_date=datetime.now(),
            )
            for _ in range(random.randint(0, 5)):
                random_index = random.randint(0, num_advertisements - 1)

                # Retrieve a single random Advertisement object:
                random_advertisement = Advertisement.objects.all()[random_index]
                Donation.objects.create(
                    donor=profile,
                    advertisement=Advertisement.objects.get(id = 4),
                    amount=self.fake.random_number(fix_len=False) / 10,
                    donated_at=datetime.now(),
                )
