# Base image
FROM python:3.12.0-slim-bookworm

# Environment variables
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Change the working directory
WORKDIR $APP

# Copy the requirements.txt to the container
COPY requirements.txt $APP

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application files to the container
COPY . $APP

# Expose the application port
EXPOSE 8000

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint and command to run the application
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
