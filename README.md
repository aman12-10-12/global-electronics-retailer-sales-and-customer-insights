# Global Electronics Retailer: Sales & Customer Insights

![Global Electronics Retailer project cover](assets/project-cover.png)

## Table of contents

- [Project background](#project-background)
- [Project objective](#project-objective)
- [Tools and workflow](#tools-and-workflow)
- [Repository structure](#repository-structure)
- [Data structure](#data-structure)
- [Executive summary](#executive-summary)
- [Sales insights](#sales-insights)
- [Customer insights](#customer-insights)
- [Recommendations](#recommendations)
- [Project resources](#project-resources)
- [Notes and limitations](#notes-and-limitations)

## Project background

Global Electronics Retailer is a fictional global business that sells a wide range of electronic products across multiple countries. The available data captures sales transactions, customer demographics, product information, store details, and exchange rates. Together, these datasets provide a complete view of how the business performs across products, locations, and customer segments.

The purpose of this project is to convert raw retail data into practical business insights. The workflow begins with cleaning and preparing the source datasets in Python, loading the cleaned data into SQL Server, analysing the data through SQL, and presenting the final findings in an interactive Excel dashboard.

The analysis focuses on revenue distribution, market performance, customer demographics, repeat purchases, retention trends, and sales patterns across high-ticket and low-ticket products. These insights can support better product strategy, targeted marketing, customer retention initiatives, and geographic expansion decisions.

## Project objective

This project answers the following business questions:

- Which product categories and individual products generate the highest revenue and profit?
- Which countries contribute the most to total sales?
- How do revenue and profit change over time?
- What are the most important customer demographics and purchasing behaviours?
- How frequently do customers return and make repeat purchases?
- Which product categories and markets offer opportunities for improvement?

## Tools and workflow

The project uses the following tools:

- **Python and Jupyter Notebook** for cleaning and preparing the raw datasets.
- **Microsoft SQL Server** for storing the cleaned data.
- **SQL** for joining tables, creating calculated fields, and preparing an analysis-ready dataset.
- **Microsoft Excel** for building an interactive dashboard containing sales and customer metrics.

The project workflow follows four stages:

1. Clean the customer, product, sales, store, and exchange-rate datasets.
2. Load the cleaned datasets into SQL Server.
3. Use SQL to join the tables and calculate revenue, profit, customer status, age groups, and order frequency.
4. Build Excel dashboards that communicate the most important sales and customer insights.

## Repository structure

```text
├── [01] ETL/
│   ├── Dataset/                         # Original source datasets
│   ├── Cleaned Datasets/                # Cleaned datasets used for analysis
│   ├── Customer Data Cleaning.ipynb
│   ├── Products Data Cleaning.ipynb
│   ├── Sales Data Cleaning.ipynb
│   ├── Stores Data Cleaning.ipynb
│   ├── Exchange Rates Data Cleaning.ipynb
│   ├── Database Creation.sql            # SQL Server database creation script
│   └── ETL.py                           # Data-loading script
│
├── [02] SQL/
│   └── revenue_customer_analysis.sql    # Revenue and customer analysis query
│
├── [03] Excel Dashboard/
│   ├── Load Data from SQL Server.md
│   ├── Revenue Metrics.md
│   ├── Customer Metrics.md
│   ├── Additional Columns.md
│   └── Global Electronics Retailer Sales and Customer Dashboard.xlsx
│
├── assets/
│   ├── project-cover.png
│   ├── er-diagram.png
│   ├── sales-dashboard.png
│   └── customer-dashboard.png
│
└── README.md
```

## Data structure

The Global Electronics Retailer database consists of five connected tables: `customers`, `sales`, `products`, `stores`, and `exchange_rates`. The dataset contains a total of 62,885 records and supports analysis of transactions, product performance, customer behaviour, store activity, and currency conversion.

The `sales` table is the central transaction table. It connects customer purchases with products, stores, and exchange-rate information.

![Entity-relationship diagram](assets/er-diagram.png)

The `customers` table contains customer demographic and location fields, including gender, city, state, country, continent, and birthday. The `products` table contains product names, brands, colours, categories, unit costs, and selling prices. The `stores` table provides store location, size, and opening-date details. The `exchange_rates` table supports currency conversion based on the transaction date and currency code. The `sales` table records orders, line items, order dates, delivery dates, quantities, customers, stores, products, and currencies.

## Executive summary

### Overview of findings

The analysis shows that desktop PCs, particularly the **WWI Desktop PC2.33 X2330 Black**, are the strongest-performing products. These products contribute significantly to total revenue, with limited variation in performance across colour options.

The computers category is the business’s largest category, generating **$19.3M in revenue** and **$12.28M in profit**. In contrast, games and toys generate the lowest revenue and profit at **$724.83K** and **$396.67K**, respectively. This difference highlights stronger demand for high-value technology products than for lower-priced entertainment products.

Home appliances have the highest average order value at **$1.84K**, showing that customers are willing to spend more on premium household technology products. The United States is the company’s strongest market, generating **$29.87M** in revenue, while France contributes the lowest revenue at **$1.52M**.

Revenue peaked in **2019**, when the company generated **$18.26M in revenue** and **$10.70M in profit**. The decline in 2021 should be interpreted carefully because the available dataset for that year is incomplete and may also reflect the impact of COVID-19.

The completed Excel dashboard can be downloaded from the [`[03] Excel Dashboard`](./%5B03%5D%20Excel%20Dashboard/) folder.

## Sales insights

![Global Electronics Retailer sales dashboard](assets/sales-dashboard.png)

The sales dashboard summarises total revenue, total profit, total orders, total units sold, sales growth, product performance, category performance, country-level revenue, and yearly revenue and profit trends.

### Top products by revenue and profit

Desktop PCs dominate the product rankings. The **WWI Desktop PC2.33 X2330 Black** is the highest-performing product, generating approximately **$505.45K in revenue** and **$337K in profit**. Other desktop PC colour variations also appear in the top five products, demonstrating that desktop computers are a consistent revenue driver rather than a one-product anomaly.

This finding suggests that the retailer should continue investing in desktop PC product lines through product development, promotion, inventory planning, and customer targeting.

### Revenue and profit by category

The computers category is the leading category, generating **$19.3M in revenue** and **$12.28M in profit**. This demonstrates strong demand for high-ticket technology products.

Games and toys are the weakest category, generating **$724.83K in revenue** and **$396.67K in profit**. The lower performance of this category suggests a possible need for improved promotion, product bundling, seasonal campaigns, or revised pricing strategies.

### Average order value by category

Home appliances generate the highest average order value at **$1.84K**. By comparison, games and toys have an average order value of only **$102.65**.

This difference creates an opportunity for the company to focus on premium product positioning, bundle offers, financing options, and targeted marketing for high-value categories such as home appliances, computers, and TV and video products.

### Revenue by country

The United States is the strongest market, generating **$29.87M in revenue**. France is the lowest-performing market, generating **$1.52M**.

The United States is therefore critical to the company’s overall performance and should remain a priority for customer retention, product availability, and marketing investment. At the same time, lower-performing markets such as France may benefit from more localised promotional campaigns, pricing reviews, and strategic partnerships.

### Revenue and profit by year

Revenue reached its highest level in **2019**, with **$18.26M in sales** and **$10.70M in profit**. Revenue and profit declined after 2019, with 2021 recording only **$1.04M in revenue** and **$61K in profit**.

The 2021 values should not be treated as a complete year-over-year comparison because the dataset contains incomplete records for that period. However, the trend still highlights the importance of monitoring sales changes over time and responding quickly to shifts in customer demand.

## Customer insights

![Global Electronics Retailer customer dashboard](assets/customer-dashboard.png)

The customer dashboard analyses total customers, new customer acquisition, average age, order frequency, customer geography, age distribution, gender distribution, repeat purchase behaviour, retention, and order frequency.

### Customer demographics

The customer base includes **11,887 unique customers**. Seniors are the largest age group, with **6,837 customers**, followed by adults with **2,659 customers** and young adults with **2,391 customers**.

This distribution indicates that the retailer has a strong customer base among older consumers. Product recommendations, communication channels, website accessibility, and promotional campaigns should consider the needs and preferences of this important segment.

The gender distribution is nearly balanced, with **51% male customers** and **49% female customers**. This balanced split suggests that the retailer serves a broad market and can use inclusive marketing strategies across product categories.

### Customer geography

The United States has the largest number of customers at **5,706**, followed by the United Kingdom with **1,570**, Canada with **1,179**, and Germany with **1,150**. Other customer contributions come from Australia, the Netherlands, Italy, and France.

This customer distribution supports the sales analysis: the United States is not only the highest-revenue country but also the country with the largest customer base.

### Repeat customers and retention

The dashboard shows a repeat customer rate of **53.40%**, indicating that more than half of customers return for additional purchases. This is a positive sign of customer loyalty and provides an opportunity to strengthen loyalty programmes, personalised offers, and repeat-purchase campaigns.

Retention reached its highest level in **2019** at **89.45%**. Retention then fluctuated and declined to **9.37% in 2021**. As with revenue trends, the 2021 value should be interpreted carefully because of incomplete data.

### Order frequency

Most customers, **10,273**, place between 1 and 9 orders. Only a very small group of customers place 30 or more orders.

This pattern suggests that the business has a large number of low-frequency buyers. Encouraging these customers to purchase more often through loyalty rewards, bundles, subscriptions, personalised recommendations, and post-purchase engagement could improve customer lifetime value.

## Recommendations

1. **Prioritise high-margin product lines.** Continue investing in desktop PCs and other high-value product categories that make the largest contribution to revenue and profit.

2. **Increase repeat purchases.** Use loyalty programmes, personalised offers, and post-purchase campaigns to convert low-frequency customers into repeat buyers.

3. **Grow underperforming categories.** Test bundles, seasonal promotions, and targeted marketing for lower-performing categories such as games and toys.

4. **Expand selectively by market.** Maintain focus on the United States while testing market-specific campaigns in lower-revenue countries.

5. **Improve retention monitoring.** Track retention by customer segment and purchase history to identify churn risk earlier.

## Skills demonstrated

- Data cleaning and transformation with Python
- Relational data modelling and SQL Server loading
- SQL joins, calculated fields, and customer segmentation
- Revenue, profitability, retention, and customer analysis
- Excel dashboard design and business storytelling

## Notes

- This project uses fictional retail data for portfolio and analytical demonstration purposes.
- The Excel workbook can be downloaded from the [`[03] Excel Dashboard`](./%5B03%5D%20Excel%20Dashboard/) folder.