import pandas as pd

# Load the dataset
file_path = r"C:\Users\Public\Documents\sales_data.xlsx"
sales_data = pd.read_excel(file_path)

# Display the first few rows of the dataset to understand its structure
sales_data.head(), sales_data.info()

import matplotlib.pyplot as plt

# Convert 'DATE' to datetime format
sales_data['DATE'] = pd.to_datetime(sales_data['DATE'])

# Extract year and month for trend analysis
sales_data['YearMonth'] = sales_data['DATE'].dt.to_period('M')

# Group by YearMonth and sum the GROSS AMT to get total sales per month
monthly_sales = sales_data.groupby('YearMonth')['GROSS AMT'].sum().reset_index()

# Plot the monthly sales trends
plt.figure(figsize=(14, 7))
plt.plot(monthly_sales['YearMonth'].astype(str), monthly_sales['GROSS AMT'], marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.show()

monthly_sales

# Plot the distribution of product prices (RATE)
plt.figure(figsize=(14, 7))
plt.hist(sales_data['RATE'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Product Prices')
plt.xlabel('Price per Unit')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot the distribution of customer spending habits (GROSS AMT)
plt.figure(figsize=(14, 7))
plt.hist(sales_data['GROSS AMT'], bins=50, color='lightgreen', edgecolor='black')
plt.title('Distribution of Customer Spending')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Summary statistics for product prices and customer spending
price_stats = sales_data['RATE'].describe()
spending_stats = sales_data['GROSS AMT'].describe()
price_stats, spending_stats


