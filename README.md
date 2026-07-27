# echochain-project

A planned data pipeline project for collecting, processing, and visualizing data — built as part of my Data Analytics internship focus areas.

## Project Overview

EchoChain is designed to demonstrate an end-to-end data engineering workflow:
raw data collection → distributed processing → reliable storage → business intelligence reporting.

## Tech Stack

- **Scrapy** – web scraping / data collection
- **PySpark** – distributed data processing
- **Databricks** – cloud-based Spark environment for transformation and orchestration
- **Delta Lake** – reliable, versioned data storage layer
- **Power BI** – dashboarding and visualization

# EchoChain – Week 1
## Circular Economy & Secondary Market Lifecycle Analytics

### Project Overview

EchoChain is a data engineering project focused on helping manufacturers analyze the lifecycle of products after they are sold. By collecting secondary market data and combining it with internal manufacturing data, the project aims to identify refurbishment opportunities, improve sustainability, and support circular economy initiatives. :contentReference[oaicite:0]{index=0}

---

# Week 1 Objectives

- Build the data acquisition pipeline.
- Collect secondary market product listings.
- Prepare the raw dataset for the data lake.
- Set up the initial project structure.

---

# Technologies Used

- Python 3.x
- PySpark
- Scrapy (or provided scraped dataset)
- Databricks (planned)
- Delta Lake (planned)

---

# Dataset

The project uses a scraped eBay listings dataset containing:

- Product ID
- Product Title
- Brand
- Condition
- Resale Price
- Seller Location

This dataset represents products available in the secondary electronics market and serves as the project's raw data source.

---

Week 1 Workflow

Secondary Market Listings
          │
          ▼
     Data Collection
          │
          ▼
     Raw CSV Dataset
          │
          ▼
    Spark Data Loading

Tasks Completed

1. Environment Setup

- Installed Python
- Installed PySpark
- Created SparkSession
- Configured project folders

 2. Data Collection

Collected secondary market product listings from the provided dataset.

Loaded the CSV file into PySpark.


3. Data Verification

Verified:

- Dataset loaded successfully
- Column names
- Data types
- Sample records

 Folder Structure

EchoChain/
│
├── data/
│   └── scraped_ebay_listings.csv
│
├── notebooks/
│   └── Week1.ipynb
│
├── src/
│   └── load_data.py
│
└── README.md

---

 Expected Output

At the end of Week 1:

- Raw eBay dataset successfully loaded.
- Spark environment configured.
- Dataset ready for cleaning and transformation in Week 2.

# Next Steps (Week 2)

- Remove duplicate records.
- Handle missing values.
- Standardize product titles.
- Extract SKUs.
- Store cleaned data in the Silver layer.



