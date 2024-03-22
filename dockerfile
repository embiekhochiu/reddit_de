# Base image for Airflow
FROM apache/airflow:2.8.1

# Install praw library
RUN pip install praw

RUN pip install s3fs

# Copy environment variables from docker-compose
ENV AIRFLOW__CORE__EXECUTOR CeleryExecutor
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN postgresql+psycopg2://airflow:airflow@postgres/airflow
ENV AIRFLOW__CELERY__RESULT_BACKEND db+postgresql://airflow:airflow@postgres/airflow
ENV AIRFLOW__CELERY__BROKER_URL redis://:@redis:6379/0
ENV AIRFLOW__CORE__FERNET_KEY: ''
ENV AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
ENV AIRFLOW__CORE__LOAD_EXAMPLES: 'False'
ENV AIRFLOW__API__AUTH_BACKENDS: 'airflow.api.auth.backend.basic_auth,airflow.api.auth.backend.session'
# ... other environment variables from docker-compose

# Set working directory
WORKDIR /opt/airflow

# Set user and group (optional, based on your docker-compose setup)
USER 50000:0



# Entrypoint (optional, customize based on your needs)
CMD ["airflow", "dags", "-s"]