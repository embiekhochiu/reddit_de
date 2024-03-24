# **Data Pipeline Project Documentation**
## **A data pipeline solution streamline the process of extracting, transforming, and loading (ETL) Reddit data to AWS Cloud Service**

### **Description**
This pipeline utilizes a comprehensive set of tools and services, incorporating Apache Airflow for workflow orchestration to pull daily data using Reddit API. The pipeline uses Celery for task queuing, PostgreSQL for data staging, Amazon S3 for the cloud storage, AWS Glue and AWS Athena for the cloud data transformation, and Amazon Redshift for data warehouse. Docker is utilized to install and run Apache Airflow, ensuring a consistent and isolated environment for workflow management.

### **Workflow Of The Project**
- Configure Dockerfile and Docker Compose to set up appropriate environment for Airflow and its volumes.
- Configure information for the database, file paths, api keys, ETL setting and AWS.
- Define DAG inside Airflow to pull daily data from Reddit using Reddit API and praw package and upload the data collected to the AWS S3 bucket.
- Access AWS end-user interface to process steps involved using cloud service.

###  **System Architecture**

![image](https://github.com/embiekhochiu/reddit_de/assets/150108017/ace3efe8-62bb-4e62-82fe-c62dbd594ddb)

- Reddit API: Source of the data.
- Apache Airflow & Celery: Orchestrates the ETL process and manages task distribution.
- PostgreSQL: Temporary storage.
- Amazon S3: Data storage.
- AWS Glue: Data cataloging and ETL jobs.
- Amazon Athena: SQL-based data transformation.
- Amazon Redshift: Data warehousing and analytics.

### **Prerequisites**
- Docker (https://docs.docker.com/get-docker/)
- AWS account
- Reddit API credentials (https://www.reddit.com/wiki/api/)

### **Installation and Setup**

**Setting up Docker and Apache Airflow**

Instruction link: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

**Congigure AWS Service**

Instruction for setting up AWS S3, AWS Glue, AWS Athena, and Amazon Redshift.
Guidlines for securing and configuring AWS environment and necessary permission for IAM roles.
Link: https://docs.aws.amazon.com/

### **Usage**
- Clone the repository.
- Create and configure config file:
  - Go to File > New File from the menu, or use the shortcut Ctrl + N (Windows/Linux) or Cmd + N (MacOS) to create a new file.
  - Configure the file as shown:
    
    ```[database]
    database_host = 
    database_name = 
    database_port = 5432
    database_username = 
    database_password = 
    
    [file_paths]
    input_path = /opt/airflow/data/input
    output_path = /opt/airflow/data/output
    
    [api_keys]
    reddit_secret_key = 
    reddit_client_id = 
    
    [aws]
    aws_access_key_id = 
    aws_secret_access_key= 
    aws_region =
    aws_bucket_name = 
    
    [etl_settings]
    batch_size = 100
    error_handling = abort
    log_level = info```

- Install all the dependencies used in source code, using the below command in terminal
  `pip install + [package_name]`

- Build image from dockerfile and start the container by typing in the terminal
  ` docker build`
  ` docker-compose up -d`

- Launch the Airflow web user interface by accessing Docker Desktop or using this command
  ` open http://localhost:8080`
    
       

  



 
