# Global Electronics Retailer: Sales & Customer Insights

![Project cover](assets/project-cover.png)

An end to end data analytics project that transforms global electronics retail data into business insights using Python, SQL Server, and Excel.

## Project overview

This project analyses sales transactions, customer behaviour, products, stores, and exchange rates for a fictional global electronics retailer. The goal is to identify revenue drivers, customer trends, and market opportunities through a reproducible data workflow and an interactive Excel dashboard.

## Business questions

- Which products, categories, and markets generate the most revenue and profit?
- How do sales and profit change over time?
- What does the customer base look like by age, gender, and geography?
- How strong are repeat purchase and retention trends?
- Which areas offer the greatest opportunity for growth?

## Tools used

- **Python and Jupyter Notebook** — data cleaning
- **SQL Server and SQL** — data storage and analysis
- **Microsoft Excel** — interactive dashboard and reporting

## Project workflow

1. Clean raw customer, product, sales, store, and exchange-rate data.
2. Load cleaned datasets into SQL Server.
3. Create an analysis-ready dataset with SQL.
4. Build sales and customer dashboards in Excel.

## Repository guide

- [`[01] ETL`](./%5B01%5D%20ETL/) — source data, cleaned data, notebooks, and loading scripts
- [`[02] SQL`](./%5B02%5D%20SQL/) — SQL analysis query
- [`[03] Excel Dashboard`](./%5B03%5D%20Excel%20Dashboard/) — dashboard workbook and metric documentation

## Data structure

The analysis combines five related tables containing **62,885 sales records**.

![Entity-relationship diagram](assets/er-diagram.png)

| Table | Description |
|---|---|
| `customers` | Customer demographics and location details |
| `sales` | Order-level transaction records |
| `products` | Product, brand, category, cost, and price information |
| `stores` | Store location, size, and opening-date details |
| `exchange_rates` | Daily currency conversion rates |

The `sales` table is the central fact table and links to customers, products, stores, and exchange rates.

## Sales performance

![Sales dashboard](assets/sales-dashboard.png)

### Key metrics

| Metric | Result |
|---|---:|
| Total revenue | $55.76M |
| Total profit | $32.66M |
| Total orders | 26,326 |
| Total units sold | 197,757 |

### Key findings

- **Computers** are the leading category, generating approximately **$19.3M** in revenue.
- The **WWI Desktop PC2.33 X2330 Black** is the highest-revenue product, delivering approximately **$505K** in revenue.
- **Home appliances** have the highest average order value at approximately **$1.84K**.
- The **United States** is the largest market, contributing approximately **$29.87M** in revenue.
- Revenue peaked in **2019** at approximately **$18.26M**.
- The 2021 figures should be interpreted carefully because the available data is incomplete.