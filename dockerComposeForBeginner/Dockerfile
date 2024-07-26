FROM python:3.12.4-alpine3.20
LABEL authors="camiloyate"

#Ww need curl for the health check
RUN apk --no-cache and curl


WORKING /app

#First, copy dependencies only \
COPY requirements.txt .

#Install dependencies
RUN pip install -r requirements.txt

#Copying the app source reparately significantly improves
#build time by using the cache if no new dependencies are added
COPY app.py .