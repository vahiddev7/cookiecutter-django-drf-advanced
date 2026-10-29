from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.views.api.v1.login import LoginView
from apps.authentication.views.api.v1.register import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    # Keep the token endpoint for backwards compatibility.
    path("token/", LoginView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
