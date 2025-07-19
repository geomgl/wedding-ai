# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for tesseract and others)
RUN apt-get update && \
    apt-get install -y tesseract-ocr libmagic1 && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY src/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Switch to working directory inside src
WORKDIR /app/src

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the main agent
CMD ["python", "main.py"]
