import pytest
from django.core.cache import cache
from django.test import override_settings
from rest_framework.test import APIClient


THROTTLE_SETTINGS = {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "login": "1/minute",
        "register": "1/minute",
    },
}


@pytest.mark.django_db
@override_settings(REST_FRAMEWORK=THROTTLE_SETTINGS)
def test_login_is_rate_limited():
    cache.clear()
    client = APIClient()
    payload = {"username": "unknown-user", "password": "invalid-password"}

    first_response = client.post("/api/auth/login/", payload, format="json")
    second_response = client.post("/api/auth/login/", payload, format="json")

    assert first_response.status_code == 401
    assert second_response.status_code == 429
    cache.clear()


@pytest.mark.django_db
@override_settings(REST_FRAMEWORK=THROTTLE_SETTINGS)
def test_registration_is_rate_limited():
    cache.clear()
    client = APIClient()
    payload = {
        "username": "throttle-user",
        "email": "throttle@example.com",
        "password": "Unique-Strong-Password-927!",
    }

    first_response = client.post("/api/auth/register/", payload, format="json")
    second_response = client.post(
        "/api/auth/register/",
        {**payload, "username": "another-user", "email": "another@example.com"},
        format="json",
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 429
    cache.clear()
