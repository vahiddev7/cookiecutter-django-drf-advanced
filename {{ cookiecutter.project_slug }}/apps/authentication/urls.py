from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.authentication.views.api.v1.register import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # Keep the token endpoint for backwards compatibility; login is an alias.
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
