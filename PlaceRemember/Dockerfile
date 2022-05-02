# Instructing Docker to use the official python3 image with dockerhub as the base image
FROM python:3
# Output from python will be sent directly to the terminal without pre-buffering
ENV PYTHONUNBUFFERED 1
# Create directory
RUN mkdir /app
# Sets the working directory of the container — "app" & add requirements.txt
WORKDIR /app
ADD requirements.txt /app/
# Installing all libs from requirements.txt
RUN pip install -r requirements.txt
# Copy all files from local project to a container
ADD . /app/
# Set parameters for cmd
CMD ["python", "manage.py", "runserver", "localhost:8000"]
# Performing migrations
RUN python manage.py migrate
