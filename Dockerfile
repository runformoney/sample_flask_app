# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8091

# Declare a build argument for DATABASE_URI
ARG DATABASE_URI

# Define environment variable
ENV DATABASE_URI $DATABASE_URI

# Run app.py when the container launches
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8091"]
