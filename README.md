# **Data Pipeline Project Documentation**
## **A data pipeline solution streamline the process of extracting, transforming, and loading (ETL) Reddit data to AWS Cloud Service**

### **Description**
This pipeline utilizes a comprehensive set of tools and services, incorporating Apache Airflow for workflow orchestration to pull daily data using Reddit API. The pipeline uses Celery for task queuing, PostgreSQL for data staging, Amazon S3 for the cloud storage, AWS Glue and AWS Athena for the cloud data transformation, and Amazon Redshift for data warehouse. Docker is utilized to install and run Apache Airflow, ensuring a consistent and isolated environment for workflow management.

### **Workflow of the project**
- Configure Dockerfile and Docker Compose to set up appropriate environment for Airflow and its volumes.
- Configure information for the database, file paths, api keys, ETL setting and AWS.
- Define DAG inside Airflow to pull daily data from Reddit using Reddit API and praw package and upload the data collected to the AWS S3 bucket.
- Access AWS end-user interface to configure



 
