# Use a smaller base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies first (leverage layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
