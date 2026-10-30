import pytest
from django.db import IntegrityError, transaction

from apps.users.models import User


@pytest.mark.django_db
def test_user_save_normalizes_email():
    user = User.objects.create_user(
        username="normalized-user",
        email="  Mixed.Case@Example.COM  ",
        password="test-password",
    )

    assert user.email == "mixed.case@example.com"


@pytest.mark.parametrize(
    "email",
    [
        "Mixed.Case@example.com",
        " mixed.case@example.com ",
    ],
)
@pytest.mark.django_db
def test_database_rejects_non_normalized_email_updates(email):
    user = User.objects.create_user(
        username="database-constraint-user",
        email="canonical@example.com",
        password="test-password",
    )

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            User.objects.filter(pk=user.pk).update(email=email)
