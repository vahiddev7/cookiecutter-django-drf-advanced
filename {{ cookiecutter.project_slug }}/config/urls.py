from django.contrib import admin
from django.urls import path
{% if cookiecutter.use_swagger == 'y' -%}
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
{%- endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
    {% if cookiecutter.use_swagger == 'y' -%}
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
{%- endif %}
]
