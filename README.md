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

# EchoChain – Week 2

Data Cleaning, Transformation & Analytics Layer (Silver → Gold)
Project Overview

Week 2 of the EchoChain project focuses on transforming raw secondary market data into structured, analysis-ready datasets. This phase introduces data cleaning, standardization, and feature engineering, followed by generating business-level insights using aggregated datasets.

The goal is to move data from the Raw Layer (Bronze) to:

Silver Layer → Cleaned and standardized dataset
Gold Layer → Aggregated, analytics-ready dataset for reporting

# Week 2 Objectives

Clean and preprocess raw eBay dataset
Handle missing and inconsistent values
Standardize product information (titles, brands)
Remove duplicate records
Perform feature extraction (SKU, keywords, pricing insights)
Generate aggregated datasets for business analysis

# Technologies Used

Python 3.x
PySpark
Databricks (planned integration)
Delta Lake (planned storage layer)
Input Dataset

Source:
data/scraped_ebay_listings.csv

Columns:

Product ID
Product Title
Brand
Condition
Resale Price
Seller Location
Week 2 Workflow

Raw Dataset (Bronze)
│
▼
Data Cleaning & Validation
│
▼
Standardization & Feature Engineering
│
▼
Silver Dataset (Cleaned Data)
│
▼
Aggregation & Business Logic
│
▼
Gold Dataset (Insights Ready)

# Tasks Completed
1. Data Cleaning
Removed duplicate records
Handled missing/null values
Corrected inconsistent data formats
Cleaned text fields (Product Title, Brand)

2. Data Standardization
Standardized brand names (e.g., HP → hp, Dell → dell)
Normalized product titles (removed special characters, extra spaces)
Converted price column to proper numeric format

3. Feature Engineering
Extracted keywords from product titles
Derived structured attributes like:
Product category
Model references
Prepared fields for future SKU matching

4. Silver Layer Creation
Generated cleaned dataset
Ensured schema consistency
Saved processed data for further analysis

5. Gold Layer Creation (Analytics)

Created aggregated insights such as:

Average resale price by brand
Product count by condition
Price distribution across locations
Most frequently listed brands
Folder Structure (Updated)

EchoChain/
│
├── data/
│ └── scraped_ebay_listings.csv
│
├── notebooks/
│ └── Week1.ipynb
│
├── src/
│ ├── load_data.py
│ └── week2_silver_gold.py
│
├── output/
│ ├── silver_data.csv
│ └── gold_data.csv
│
└── README.md


At the end of Week 2:
Raw dataset successfully cleaned and standardized.
SKU extracted from product titles for structured analysis.
Silver dataset created with valid and filtered records.
Gold dataset generated by joining with BOM data.
Final dataset exported for Power BI visualization.



