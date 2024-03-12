# Base image for Airflow
FROM apache/airflow:2.8.1

# Install praw library
RUN pip install praw

# Copy environment variables from docker-compose
ENV AIRFLOW__CORE__EXECUTOR CeleryExecutor
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN postgresql+psycopg2://airflow:airflow@postgres/airflow
ENV AIRFLOW__CELERY__RESULT_BACKEND db+postgresql://airflow:airflow@postgres/airflow
ENV AIRFLOW__CELERY__BROKER_URL redis://:@redis:6379/0
# ... other environment variables from docker-compose

# Set working directory
WORKDIR /opt/airflow

# Set user and group (optional, based on your docker-compose setup)
USER 50000:0



# Entrypoint (optional, customize based on your needs)
CMD ["airflow", "dags", "-s"]