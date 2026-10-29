import pytest

from apps.authentication.serializers.register import RegisterSerializer
from apps.users.models import User


def test_registration_requires_email():
    serializer = RegisterSerializer(
        data={
            "username": "missingemail",
            "password": "Violet-Telescope-94!River",
        }
    )

    assert not serializer.is_valid()
    assert "email" in serializer.errors


@pytest.mark.django_db
def test_registration_creates_user_with_email():
    serializer = RegisterSerializer(
        data={
            "username": "registrationtest",
            "email": "registration@example.com",
            "password": "Violet-Telescope-94!River",
        }
    )

    assert serializer.is_valid(), serializer.errors
    user = serializer.save()

    assert isinstance(user, User)
    assert user.email == "registration@example.com"
    assert user.check_password("Violet-Telescope-94!River")
