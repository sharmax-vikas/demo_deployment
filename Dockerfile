FROM python:3.12.6-slim

# Set working directory to root
WORKDIR /

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# Run command
CMD ["streamlit", "run", "app.py"]