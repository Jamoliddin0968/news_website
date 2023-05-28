# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get install -y git
RUN git init
RUN apt-get install -y gcc python3-dev
RUN apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev
RUN apt-get install -y default-mysql-client default-libmysqlclient-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code to the container
COPY . /code/

# Expose the Django port
EXPOSE 8000

# Start the Django development server
CMD ["gunicorn", "config.wsgi:application", "--bind","--workers", "3", "0.0.0.0:8000"]
