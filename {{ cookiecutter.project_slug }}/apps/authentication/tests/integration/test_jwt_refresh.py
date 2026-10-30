import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_refresh_rotates_token_and_blacklists_previous_token():
    get_user_model().objects.create_user(
        username="refresh-user",
        email="refresh@example.com",
        password="Unique-Strong-Password-927!",
    )
    client = APIClient()
    login_response = client.post(
        "/api/auth/login/",
        {
            "username": "refresh-user",
            "password": "Unique-Strong-Password-927!",
        },
        format="json",
    )

    assert login_response.status_code == 200
    original_refresh = login_response.data["refresh"]

    refresh_response = client.post(
        "/api/auth/token/refresh/",
        {"refresh": original_refresh},
        format="json",
    )

    assert refresh_response.status_code == 200
    rotated_refresh = refresh_response.data["refresh"]
    assert rotated_refresh != original_refresh
    assert "access" in refresh_response.data

    reuse_response = client.post(
        "/api/auth/token/refresh/",
        {"refresh": original_refresh},
        format="json",
    )

    assert reuse_response.status_code == 401


@pytest.mark.django_db
def test_refresh_returns_new_access_token():
    get_user_model().objects.create_user(
        username="access-user",
        email="access@example.com",
        password="Unique-Strong-Password-927!",
    )
    client = APIClient()
    login_response = client.post(
        "/api/auth/login/",
        {
            "username": "access-user",
            "password": "Unique-Strong-Password-927!",
        },
        format="json",
    )

    refresh_response = client.post(
        "/api/auth/token/refresh/",
        {"refresh": login_response.data["refresh"]},
        format="json",
    )

    assert refresh_response.status_code == 200
    assert refresh_response.data["access"]
