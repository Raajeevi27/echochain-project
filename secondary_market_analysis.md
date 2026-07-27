# Secondary Market Analysis

This document summarizes the exploratory analysis performed on the cleaned secondary marketplace dataset used in the EchoChain project.

The objective is to understand product resale trends and prepare the dataset for advanced analytics and Power BI reporting.

## Dataset Information

Total Records: 200

Source: Cleaned secondary marketplace listings

Purpose:
- Analyze resale market
- Identify pricing trends
- Support Circular Economy analytics

## Dataset Columns

| Column | Description |
|---------|-------------|
| product_id | Unique identifier of each product listing |
| title | Product title scraped from marketplace |
| condition | Condition of the listed product |
| resale_price | Selling price of the product |
| location | Seller location |
| title_word_count | Number of words in title |
| title_length | Total characters in title |
| price_category | Low / Medium / High price segment |

## Exploratory Analysis Performed

The following analyses were completed:

- Product condition distribution
- Listings by location
- Resale price distribution
- Average resale price by condition
- Highest priced listings
- Average resale price by location

## Business Insights

The analysis helps identify:

- Locations with higher resale activity.
- Product conditions associated with higher resale prices.
- Price segmentation for marketplace listings.
- Valuable resale opportunities for circular economy initiatives.

## Future Work

Remaining development includes:

- Fuzzy matching between marketplace titles and internal SKU database.
- Circularity Score calculation.
- Integration with Power BI dashboards.
- Executive reporting.

## Related Files

- notebooks/01_data_profiling.ipynb
- notebooks/02_marketplace_visualization.ipynb
- notebooks/03_feature_engineering.ipynb
- notebooks/04_business_insights.ipynb