FROM python:3.12-slim

WORKDIR /app

{% if cookiecutter.database_engine == 'sqlserver' %}
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl gnupg ca-certificates unixodbc-dev libgssapi-krb5-2 \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/microsoft-prod.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*
{% endif %}

COPY requirements/ /app/requirements

RUN pip install --no-cache-dir -r /app/requirements/production.txt

COPY . /app/

EXPOSE 8000

RUN chmod +x /app/docker/production/entrypoint.sh
CMD ["./docker/production/entrypoint.sh"]
