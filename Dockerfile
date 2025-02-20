FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy script and requirements
COPY postgres_backup.py /app/postgres_backup.py

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Set environment variables (can be overridden at runtime)
ENV DB_NAME=""
ENV DB_USER=""
ENV DB_PASSWORD=""
ENV DB_HOST="localhost"
ENV DB_PORT="5432"
ENV BACKUP_DIR="/backups/"

# Create backup directory
RUN mkdir -p $BACKUP_DIR

# Set entrypoint
ENTRYPOINT ["python", "/app/postgres_backup.py"]