# Use official Python image
FROM python:3.12

# Set working directory inside container
WORKDIR /app

# Copy project files to container
COPY . .

# Upgrade pip to latest version
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Install Node.js & Prettier for formatting
RUN apt-get update && apt-get install -y nodejs npm
RUN npm install -g prettier@3.4.2  # Install specific Prettier version
# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
