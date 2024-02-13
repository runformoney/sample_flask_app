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

# Define environment variable
ENV DATABASE_URI postgresql://school_lzcu_user:2bYeUkfbdEmikpN9SqJV5Ru6OsFnyPjF@dpg-cn5tbaa1hbls73aklfl0-a.frankfurt-postgres.render.com/school_lzcu

# Run app.py when the container launches
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8091"]
