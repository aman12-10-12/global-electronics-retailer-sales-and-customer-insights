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

## Customer insights

![Customer dashboard](assets/customer-dashboard.png)

### Key metrics

| Metric | Result |
|---|---:|
| Total customers | 11,887 |
| New customers in the past 365 days | 711 |
| Average customer age | 56 years |
| Average order frequency | 2 orders |
| Customer acquisition rate | 6.33% |
| Repeat customer rate | 53.40% |

### Key findings

- Seniors represent the largest customer age group, followed by adults and young adults.
- The gender split is balanced: **51% male** and **49% female**.
- The United States has the largest customer base with **5,706** customers.
- More than **10,000 customers** place between 1 and 9 orders, indicating a major opportunity to encourage repeat purchases.
- Retention peaked at **89.45% in 2019** and declined in later years; the incomplete 2021 data should be interpreted with caution.

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