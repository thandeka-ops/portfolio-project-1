# Use an official Python runtime
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY app/requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Expose the application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]