# Base build stage, -slim for a smaller image
FROM python:3.11-slim AS build

# Create app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Upgrade pip and install system dependencies
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    pip install --upgrade pip

# Copy the files from project directory into app directory inside the docker image
COPY . /app/

# Install Python dependencies
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "gondola_booking.wsgi:application", "--bind", "0.0.0.0:8000"]