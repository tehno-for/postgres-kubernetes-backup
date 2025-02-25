# Base alpine image
FROM python:3.11-alpine3.19

# Set working directory
WORKDIR /app

# Copy script and requirements
COPY ./postgres-kubernetes-backup/postgres_backup.py /app/postgres_backup.py

# Install dependencies
RUN apk --no-cache add postgresql16-client

# Set entrypoint
CMD ["python", "/app/postgres_backup.py"]