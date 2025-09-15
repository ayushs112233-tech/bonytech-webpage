# Use Python 3.9 base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run Flask
CMD ["python", "index.py"]
