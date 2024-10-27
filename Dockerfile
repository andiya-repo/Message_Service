# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Make port 7018 available to the world outside this container
EXPOSE 7018

# Define environment variable
ENV FLASK_APP wsgi.py

# Run the application
CMD ["python", "wsgi.py"]