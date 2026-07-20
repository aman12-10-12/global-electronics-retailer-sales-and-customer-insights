# Global Electronics Retailer: Sales & Customer Insights

An end to end data analytics project that explores sales performance, customer behaviour, product demand, and store performance for a fictional global electronics retailer.

## Project goal

Transform raw retail data into actionable business insights through data cleaning, SQL analysis, and an interactive Excel dashboard.

## Questions explored

- Which product categories, products, and countries generate the most revenue and profit?
- How do sales and profit change over time?
- What are the key characteristics of the customer base?
- How frequently do customers return and make repeat purchases?
- Which markets and product categories present opportunities for growth?

## Project workflow

1. Clean the raw customer, product, sales, store, and exchange-rate datasets.
2. Load the cleaned data into a SQL Server database.
3. Analyse revenue, profit, customer, and retention metrics with SQL.
4. Present the findings in an interactive Excel dashboard.

## Repository structure

```text
├── [01] ETL/                 # Data cleaning notebooks, datasets, and database loading files
├── [02] SQL/                 # SQL analysis queries
├── [03] Excel Dashboard/     # Dashboard workbook and build documentation
└── README.md
```

## Tools used

- Python and Jupyter Notebook for data cleaning
- Microsoft SQL Server for data storage and analysis
- SQL for business analysis
- Microsoft Excel for dashboard design and reporting

## Dataset

The project uses five related datasets:

- Customers
- Products
- Sales
- Stores
- Exchange rates

## Data preparation

The raw datasets and their cleaned versions are included in the repository under `[01] ETL/`.

- `Dataset/` contains the original source files.
- `Cleaned Datasets/` contains the processed files used in the next stages of the project.
- The five Jupyter notebooks document the cleaning process for customers, products, sales, stores, and exchange rates.

## Project status

Completed:

- [x] Project documentation
- [x] Raw datasets
- [x] Data-cleaning notebooks
- [x] Cleaned datasets

Next:

- [ ] SQL Server database setup and data loading
- [ ] SQL revenue and customer analysis
- [ ] Excel dashboard and supporting documentation
