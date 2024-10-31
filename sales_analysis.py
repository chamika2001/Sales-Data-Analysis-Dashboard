# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
sales_data = pd.read_csv('sales_data.csv')  # Update with your file name

# Check for missing values
print(sales_data.isnull().sum())  # Display the count of missing values in each column

# Remove rows with missing values
sales_data = sales_data.dropna()

# Remove duplicate rows
sales_data = sales_data.drop_duplicates()

# Convert 'Order Date' to datetime format
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'], errors='coerce')

# Create a new column for total sales
# Ensure 'Quantity Ordered' and 'Price Each' are numeric
sales_data['Quantity Ordered'] = pd.to_numeric(sales_data['Quantity Ordered'], errors='coerce')
sales_data['Price Each'] = pd.to_numeric(sales_data['Price Each'], errors='coerce')
sales_data['Sales'] = sales_data['Quantity Ordered'] * sales_data['Price Each']

# Extract month from 'Order Date' and convert to integer
sales_data['Month'] = sales_data['Order Date'].dt.month.astype(int)

# Check if the 'Sales' column is numeric
print(sales_data['Sales'].dtypes)  # This should show 'float64' or 'int64'
print(sales_data['Month'].dtypes)  # This should show 'int64'

# Analyze monthly sales
monthly_sales = sales_data.groupby('Month')['Sales'].sum()  # Groups by month and sums the sales

# Print monthly sales for debugging
print(monthly_sales)  # Check the monthly sales data

# Plot monthly sales
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales in USD')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.show()  # Display the bar chart
