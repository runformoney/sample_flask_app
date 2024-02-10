# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV DATBASE_NAME database.db
ENV POSTGRES_DB school
ENV POSTGRES_HOST 192.168.0.40
ENV POSTGRES_PASSWORD welcome1
ENV POSTGRES_PORT 5432
ENV POSTGRES_USER postgres

# Run app.py when the container launches
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8080"]
