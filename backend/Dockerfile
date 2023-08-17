#Basis-Image
FROM python:3.11.3-alpine

# Arbeitsverzeichnis im Container
WORKDIR /app

RUN apk add --no-cache \
  linux-headers \
  gcc \
  musl-dev \
  postgresql-client \
  postgresql-dev \
  mailcap

# Kopiere das Requirements in den Container
COPY requirements.txt /app/

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere das Django-Projekt in den Container
COPY . /app/

ENV DJANGO_CONFIGURATION=Production DJANGO_SETTINGS_MODULE=backend.settings

# Exponiere den Port, auf dem das Django-Projekt läuft
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

# Starte das Django-Projekt
CMD ["uwsgi", "-showconfig", "/app/uwsgi.ini"]