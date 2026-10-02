FROM python:3.12-slim

WORKDIR /app

COPY requirements/ /app/requirements

RUN pip install --no-cache-dir -r /app/requirements/production.txt

COPY . /app/

EXPOSE 8000

RUN chmod +x /app/docker/production/entrypoint.sh
CMD ["./docker/production/entrypoint.sh"]
