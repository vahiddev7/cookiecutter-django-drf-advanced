from config.settings.env import env


# Keep local filesystem storage as the zero-configuration default.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

{% if cookiecutter.cloud_storage == "s3" %}
# AWS S3 (or an S3-compatible service) stores uploaded media and collected static files.
# In production, prefer IAM roles or workload identity over long-lived access keys.
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": env("AWS_STORAGE_BUCKET_NAME"),
            "location": env("AWS_MEDIA_LOCATION", default="media"),
            "region_name": env("AWS_S3_REGION_NAME", default=None),
            "endpoint_url": env("AWS_S3_ENDPOINT_URL", default=None),
            "custom_domain": env("AWS_S3_CUSTOM_DOMAIN", default=None),
            "default_acl": None,
            "file_overwrite": False,
            "querystring_auth": env.bool("AWS_QUERYSTRING_AUTH", default=True),
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": env("AWS_STORAGE_BUCKET_NAME"),
            "location": env("AWS_STATIC_LOCATION", default="static"),
            "region_name": env("AWS_S3_REGION_NAME", default=None),
            "endpoint_url": env("AWS_S3_ENDPOINT_URL", default=None),
            "custom_domain": env("AWS_S3_CUSTOM_DOMAIN", default=None),
            "default_acl": None,
            "querystring_auth": False,
        },
    },
}
{% elif cookiecutter.cloud_storage == "gcloud" %}
# Google Cloud Storage uses Application Default Credentials by default.
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": env("GS_BUCKET_NAME"),
            "location": env("GS_MEDIA_LOCATION", default="media"),
            "querystring_auth": env.bool("GS_QUERYSTRING_AUTH", default=False),
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": env("GS_BUCKET_NAME"),
            "location": env("GS_STATIC_LOCATION", default="static"),
            "querystring_auth": False,
        },
    },
}
{% elif cookiecutter.cloud_storage == "azure" %}
# Azure Blob Storage supports account keys or supported identity-based credentials.
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "azure_container": env("AZURE_MEDIA_CONTAINER", default="media"),
            "location": env("AZURE_MEDIA_LOCATION", default=""),
            "overwrite_files": False,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "azure_container": env("AZURE_STATIC_CONTAINER", default="static"),
            "location": env("AZURE_STATIC_LOCATION", default=""),
        },
    },
}
{% endif %}
