FROM docker.arvancloud.ir/python:3.12-slim

WORKDIR /app

COPY requirements/ /app/requirements

RUN pip install --trusted-host mirror2.chabokan.net -i http://mirror2.chabokan.net/pypi/simple/ \
 --no-cache-dir -r /app/requirements/production.txt

COPY . /app/

EXPOSE 8000

RUN chmod +x /app/docker/production/entrypoint.sh
CMD ["./docker/production/entrypoint.sh"]
