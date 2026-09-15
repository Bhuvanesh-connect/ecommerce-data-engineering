# E-commerce Data Engineering Pipeline

An end-to-end data engineering project that demonstrates how e-commerce order data can be ingested, processed, validated, stored, transformed, and orchestrated using commonly used data engineering technologies.

## Architecture

```text
                    E-commerce Orders
                           │
             ┌─────────────┴─────────────┐
             │                           │
        Batch Data                  Streaming Data
             │                           │
        CSV / AWS S3                 Kafka
             │                           │
             └─────────────┬─────────────┘
                           │
                    Data Processing
                  Python / Pandas
                     PySpark
                           │
                           ▼
                     Data Quality
                           │
                           ▼
                      PostgreSQL
                           │
                           ▼
                         dbt
                           │
                    ┌──────┴──────┐
                    │             │
                Fact Orders   Dimensions
                    │             │
                    └──────┬──────┘
                           │
                       Analytics

Airflow → Pipeline orchestration
Docker → Containerized services
Git/GitHub → Version control
GitHub Actions → CI checks
```

## Technologies Used

* **Python** — data ingestion and transformation
* **Pandas** — processing smaller tabular datasets
* **SQL / PostgreSQL** — data storage and querying
* **AWS S3** — object storage
* **PySpark** — distributed data processing
* **dbt** — SQL-based transformations and data modeling
* **Airflow** — workflow orchestration
* **Kafka** — streaming order events
* **Docker** — containerized services
* **Git / GitHub** — version control
* **GitHub Actions** — continuous integration
* **Databricks** — explored for large-scale Spark workloads

## Project Flow

### Batch Pipeline

```text
orders.csv
    ↓
Python
    ↓
AWS S3
    ↓
Transformation
    ↓
Data Quality Checks
    ↓
PostgreSQL
    ↓
dbt
    ↓
Fact & Dimension Models
```

### Streaming Pipeline

```text
E-commerce Application
        ↓
Python Producer
        ↓
Kafka
        ↓
orders Topic
        ↓
Python Consumer
```

## Data Model

The project uses a simple dimensional model.

### Fact Table

`fact_orders`

Contains order-level transactional information such as:

* order ID
* customer ID
* product ID
* quantity
* price
* order total
* order date

### Dimension Tables

`dim_customers`

* customer ID
* customer name
* city

`dim_products`

* product ID
* product name
* category

## Data Quality

Basic data quality checks are performed for:

* Missing values
* Invalid quantities
* Invalid prices
* Duplicate/unique key validation through dbt tests

## Orchestration

Airflow is used to demonstrate the workflow dependency:

```text
Ingest
  ↓
Transform
  ↓
Validate
  ↓
Load
```

## Kafka Streaming

Kafka is used to demonstrate real-time order events.

A Python producer sends order events to the `orders` topic, while a Python consumer reads those events.

## CI

GitHub Actions automatically runs a Python syntax check whenever code is pushed to the `main` branch.

## Project Structure

```text
ecommerce_data_engineering/
│
├── airflow/
│   ├── dags/
│   └── docker-compose.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dbt_project/
│   ├── models/
│   └── dbt_project.yml
│
├── kafka/
│   └── docker-compose.yml
│
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── quality/
│   └── loading/
│
├── .github/
│   └── workflows/
│       └── python-check.yml
│
├── .gitignore
└── README.md
```

## Purpose

The goal of this project is to understand and demonstrate the core components of a modern data engineering pipeline rather than build a production-scale system.

The project focuses on understanding how different tools fit together in a real-world data workflow.
