from django.contrib import admin
from django.urls import include, path
{% if cookiecutter.use_drf == "y" and cookiecutter.use_swagger == "y" -%}
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
{%- endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
    {% if cookiecutter.use_drf == "y" -%}
    path("api/auth/", include("apps.authentication.urls")),
    {%- endif %}
    {% if cookiecutter.use_drf == "y" and cookiecutter.use_swagger == "y" -%}
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    {%- endif %}
]
