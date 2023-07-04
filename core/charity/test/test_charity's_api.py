from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a/@1234567", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    def test_get_ad_response_200_status(self, api_client):
        url = reverse("charity:api-v1:ads-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_ad_response_401_status(self, api_client):
        url = reverse("charity:api-v1:ads-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_ad_response_201_status(self, api_client, common_user):
        url = reverse("charity:api-v1:ads-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "estimated_amount": 0,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_ad_invalid_data_response_400_status(self, api_client, common_user):
        url = reverse("charity:api-v1:ads-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400


@pytest.mark.django_db
class TestDonationApi:
    def test_create_donations_response_401_status(self, api_client):
        url = reverse("charity:api-v1:donation-list")
        data = {"advertisement": 1, "amount": 1}
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_donation_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("charity:api-v1:donation-list")
        data = {"advertisement": 1, "amount": 1}
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
