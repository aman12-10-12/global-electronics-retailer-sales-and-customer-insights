# Global Electronics Retailer: Sales & Customer Insights

*An end-to-end data analytics project focused on sales performance, customer behaviour, product demand, and store performance for a fictional global electronics retailer.*

## Project objective

- Transform raw retail data into **actionable business insights**
- Use **data cleaning**, **SQL analysis**, and an **interactive Excel dashboard**
- Identify trends in **revenue**, **profit**, **customers**, and **retention**

## Key questions

- Which products, categories, and countries generate the most revenue and profit?
- How do revenue and profit change over time?
- What are the key characteristics of the customer base?
- How frequently do customers make repeat purchases?
- Which markets and product categories present growth opportunities?

## Project workflow

1. Clean raw customer, product, sales, store, and exchange-rate data.
2. Load the cleaned datasets into SQL Server.
3. Analyse revenue, profit, customer, and retention metrics with SQL.
4. Build an interactive Excel dashboard to present the findings.

## Repository structure

```text
├── [01] ETL/
│   ├── Dataset/                      # Raw source datasets
│   ├── Cleaned Datasets/             # Cleaned datasets
│   ├── Data Cleaning Notebooks       # Cleaning workflow
│   ├── Database Creation.sql         # SQL Server database setup
│   └── ETL.py                        # Data-loading script
│
├── [02] SQL/
│   └── revenue_customer_analysis.sql  # Revenue and customer analysis query
│
├── [03] Excel Dashboard/
│   ├── Load Data from SQL Server.md
│   ├── Revenue Metrics.md
│   ├── Customer Metrics.md
│   ├── Additional Columns.md
│   └── Global Electronics Retailer Sales and Customer Dashboard.xlsx
│
└── README.md
```

## Dataset

The project uses five related datasets:

- **Customers**
- **Products**
- **Sales**
- **Stores**
- **Exchange rates**

## Data preparation

The raw and cleaned datasets are stored under `[01] ETL/`.

### Cleaning process

- Five Jupyter notebooks document the cleaning workflow for:
  - customers
  - products
  - sales
  - stores
  - exchange rates
- The cleaned outputs are prepared for:
  - SQL Server loading
  - analytical querying
  - dashboard reporting

## SQL Server setup and loading

### Database creation

- `Database Creation.sql` creates the `Global_Electronics_Retailer` database.

### Data loading

- `ETL.py` loads the cleaned:
  - customer data
  - sales data
  - store data
  - product data
  - exchange-rate data
- All datasets are inserted into SQL Server tables for analysis.

### Required environment variables

Before running the loader, configure these environment variables:

```bash
SQL_SERVER
SQL_USERNAME
SQL_PASSWORD
```

- `SQL_DATABASE` is optional and defaults to `Global_Electronics_Retailer`.

## SQL analysis

`[02] SQL/[01] revenue_customer_analysis.sql` combines the customer, sales, store, product, and exchange-rate tables into an analysis-ready dataset.

### The query calculates:

- Customer age groups
- Order date attributes
- Revenue, total cost, and profit
- New versus repeat customer status
- Customer order counts

## Excel dashboard

The completed interactive dashboard is available here:

`[03] Excel Dashboard/Global Electronics Retailer Sales and Customer Dashboard.xlsx`

### Supporting documentation includes:

- How to import SQL Server data into Excel
- How to create helper columns for order-frequency groups
- How to calculate revenue and profit metrics
- How to calculate customer and retention metrics

## Tools used

- Python
- Jupyter Notebook
- Microsoft SQL Server
- SQL
- Microsoft Excel

## Project status

- [x] Project documentation
- [x] Raw datasets
- [x] Data-cleaning notebooks
- [x] Cleaned datasets
- [x] SQL Server database setup and data loading
- [x] SQL revenue and customer analysis
- [x] Excel dashboard documentation
- [x] Interactive Excel dashboard
