import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_custom_user_model_hashes_password():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username="ci-user",
        email="ci-user@example.com",
        password="Safe-test-password-849!",
    )

    assert user.pk is not None
    assert user.check_password("Safe-test-password-849!")
    assert not user.check_password("incorrect-password")
    assert user_model._meta.app_label == "users"
