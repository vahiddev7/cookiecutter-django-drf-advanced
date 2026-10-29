import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_registration_creates_user_without_returning_password():
    response = APIClient().post(
        "/api/auth/register/",
        {
            "username": "registered-user",
            "email": "registered@example.com",
            "password": "Unique-Strong-Password-927!",
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["username"] == "registered-user"
    assert response.data["email"] == "registered@example.com"
    assert "password" not in response.data
    user = get_user_model().objects.get(username="registered-user")
    assert user.check_password("Unique-Strong-Password-927!")


@pytest.mark.django_db
def test_registration_rejects_duplicate_username():
    user_model = get_user_model()
    user_model.objects.create_user(
        username="existing-user",
        email="existing@example.com",
        password="Unique-Strong-Password-927!",
    )

    response = APIClient().post(
        "/api/auth/register/",
        {
            "username": "existing-user",
            "email": "another@example.com",
            "password": "Another-Strong-Password-927!",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "username" in response.data
