import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set styling
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (15, 10)

print("\n" + "="*80)
print("E-COMMERCE SALES ANALYSIS - COMPLETE REPORT")
print("="*80)

# Create sample data directly
data = {
    'Order_ID': ['ORD001', 'ORD002', 'ORD003', 'ORD004', 'ORD005', 'ORD006', 'ORD007', 'ORD008', 'ORD009', 'ORD010',
                 'ORD011', 'ORD012', 'ORD013', 'ORD014', 'ORD015', 'ORD016', 'ORD017', 'ORD018', 'ORD019', 'ORD020',
                 'ORD021', 'ORD022', 'ORD023', 'ORD024', 'ORD025', 'ORD026', 'ORD027', 'ORD028', 'ORD029', 'ORD030',
                 'ORD031', 'ORD032', 'ORD033', 'ORD034', 'ORD035', 'ORD036', 'ORD037', 'ORD038', 'ORD039', 'ORD040',
                 'ORD041', 'ORD042', 'ORD043', 'ORD044', 'ORD045', 'ORD046', 'ORD047', 'ORD048', 'ORD049', 'ORD050'],
    'Date': pd.date_range('2024-01-05', periods=50, freq='D'),
    'Product': ['Wireless Headphones', 'Running Shoes', 'Winter Jacket', 'Coffee Maker', 'Yoga Mat', 'Smart Watch',
                'Cotton T-Shirt', 'Desk Lamp', 'Basketball', 'Bluetooth Speaker', 'Canvas Shoes', 'Sweater',
                'Microwave Oven', 'Dumbbells Set', 'USB-C Cable', 'Formal Pants', 'Blender', 'Tennis Racket',
                'Phone Screen Protector', 'Jeans', 'Water Bottle', 'Running Socks', 'Shorts', 'Air Purifier',
                'Resistance Bands', 'Mobile Phone', 'Polo Shirt', 'Coffee Beans', 'Cricket Bat', 'Tablet',
                'Jacket', 'Vacuum Cleaner', 'Gym Bag', 'Earbuds', 'Summer Dress', 'Electric Kettle', 'Football',
                'Laptop', 'Casual Shirt', 'Toaster', 'Yoga Blocks', 'USB Hub', 'Boots', 'Hood Sweatshirt',
                'Refrigerator', 'Dumbbell', 'Monitor', 'Sneakers', 'Hoodie', 'Dishwasher'],
    'Category': ['Electronics', 'Footwear', 'Clothing', 'Home Appliances', 'Sports', 'Electronics', 'Clothing',
                 'Home Appliances', 'Sports', 'Electronics', 'Footwear', 'Clothing', 'Home Appliances', 'Sports',
                 'Electronics', 'Clothing', 'Home Appliances', 'Sports', 'Electronics', 'Clothing', 'Home Appliances',
                 'Footwear', 'Clothing', 'Home Appliances', 'Sports', 'Electronics', 'Clothing', 'Home Appliances',
                 'Sports', 'Electronics', 'Clothing', 'Home Appliances', 'Sports', 'Electronics', 'Clothing',
                 'Home Appliances', 'Sports', 'Electronics', 'Clothing', 'Home Appliances', 'Sports', 'Electronics',
                 'Footwear', 'Clothing', 'Home Appliances', 'Sports', 'Electronics', 'Footwear', 'Clothing',
                 'Home Appliances'],
    'Price': [1500, 2800, 3500, 4200, 800, 5999, 499, 1200, 1500, 2500, 1999, 2200, 6500, 3500, 399, 1800, 2800,
              4500, 299, 1500, 599, 299, 999, 8500, 1200, 15999, 1200, 499, 2500, 25000, 3000, 7500, 1500, 3500,
              2500, 1500, 800, 55000, 899, 1800, 500, 899, 3500, 1599, 25000, 500, 12000, 2200, 1800, 30000],
    'Quantity': [2, 1, 1, 1, 3, 1, 5, 2, 2, 1, 2, 1, 1, 1, 10, 2, 1, 1, 15, 3, 8, 20, 4, 1, 5, 1, 6, 10, 2, 1,
                 1, 1, 3, 2, 1, 2, 4, 1, 8, 2, 12, 6, 1, 2, 1, 15, 1, 3, 4, 1],
    'Revenue': [3000, 2800, 3500, 4200, 2400, 5999, 2495, 2400, 3000, 2500, 3998, 2200, 6500, 3500, 3990, 3600,
                2800, 4500, 4485, 4500, 4792, 5980, 3996, 8500, 6000, 15999, 7200, 4990, 5000, 25000, 3000, 7500,
                4500, 7000, 2500, 3000, 3200, 55000, 7192, 3600, 6000, 5394, 3500, 3198, 25000, 7500, 12000, 6600,
                7200, 30000],
    'Customer_ID': ['CUST101', 'CUST102', 'CUST103', 'CUST104', 'CUST105', 'CUST106', 'CUST107', 'CUST108',
                    'CUST109', 'CUST110', 'CUST111', 'CUST112', 'CUST113', 'CUST114', 'CUST115', 'CUST116',
                    'CUST117', 'CUST118', 'CUST119', 'CUST120', 'CUST101', 'CUST102', 'CUST103', 'CUST104',
                    'CUST105', 'CUST106', 'CUST107', 'CUST108', 'CUST109', 'CUST110', 'CUST111', 'CUST112',
                    'CUST113', 'CUST114', 'CUST115', 'CUST116', 'CUST117', 'CUST118', 'CUST119', 'CUST120',
                    'CUST101', 'CUST102', 'CUST103', 'CUST104', 'CUST105', 'CUST106', 'CUST107', 'CUST108',
                    'CUST109', 'CUST110'],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South',
               'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North',
               'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East',
               'West', 'North', 'South', 'East', 'West', 'North'],
    'Rating': [4.5, 4.8, 4.2, 4.6, 4.9, 4.7, 4.3, 4.4, 4.6, 4.8, 4.5, 4.7, 4.9, 4.4, 4.2, 4.6, 4.8, 4.5,
               4.3, 4.7, 4.6, 4.4, 4.8, 4.9, 4.5, 4.7, 4.6, 4.3, 4.8, 4.9, 4.4, 4.6, 4.7, 4.5, 4.8, 4.6,
               4.4, 4.9, 4.5, 4.7, 4.3, 4.6, 4.8, 4.5, 4.9, 4.4, 4.7, 4.6, 4.8, 4.5]
}

df = pd.DataFrame(data)

# Calculate additional metrics
df['Cost_Per_Unit'] = df['Price'] * 0.7
df['Total_Cost'] = df['Cost_Per_Unit'] * df['Quantity']
df['Profit'] = df['Revenue'] - df['Total_Cost']
df['Profit_Margin'] = ((df['Profit'] / df['Revenue']) * 100).round(2)

print("\n1. DATASET OVERVIEW")
print("-" * 80)
print(f"Total Records: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")

print("\n2. FIRST 10 RECORDS")
print("-" * 80)
print(df.head(10).to_string())

print("\n3. KEY PERFORMANCE INDICATORS (KPIs)")
print("-" * 80)
total_revenue = df['Revenue'].sum()
total_orders = len(df)
avg_order_value = df['Revenue'].mean()
total_items = df['Quantity'].sum()
avg_rating = df['Rating'].mean()
unique_customers = df['Customer_ID'].nunique()
total_profit = df['Profit'].sum()

print(f"Total Revenue:              Rs {total_revenue:>18,.2f}")
print(f"Total Orders:               {total_orders:>21}")
print(f"Average Order Value:        Rs {avg_order_value:>18,.2f}")
print(f"Total Items Sold:           {total_items:>21} units")
print(f"Total Profit:               Rs {total_profit:>18,.2f}")
print(f"Unique Customers:           {unique_customers:>21}")
print(f"Average Customer Rating:    {avg_rating:>21.2f}/5.0")

print("\n4. CATEGORY ANALYSIS")
print("-" * 80)
category_analysis = df.groupby('Category').agg({
    'Revenue': 'sum',
    'Order_ID': 'count',
    'Quantity': 'sum',
    'Rating': 'mean'
}).round(2)
category_analysis.columns = ['Revenue', 'Orders', 'Units_Sold', 'Avg_Rating']
category_analysis = category_analysis.sort_values('Revenue', ascending=False)
print(category_analysis.to_string())

print("\n5. REGIONAL ANALYSIS")
print("-" * 80)
region_analysis = df.groupby('Region').agg({
    'Revenue': 'sum',
    'Order_ID': 'count',
    'Customer_ID': 'nunique'
}).round(2)
region_analysis.columns = ['Revenue', 'Orders', 'Customers']
region_analysis = region_analysis.sort_values('Revenue', ascending=False)
print(region_analysis.to_string())

print("\n6. TOP 5 PRODUCTS BY REVENUE")
print("-" * 80)
top_products = df.groupby('Product').agg({
    'Revenue': 'sum',
    'Quantity': 'sum',
    'Rating': 'mean'
}).round(2)
top_products.columns = ['Revenue', 'Units_Sold', 'Avg_Rating']
top_products = top_products.sort_values('Revenue', ascending=False).head(5)
print(top_products.to_string())

print("\n7. MONTHLY SALES TREND")
print("-" * 80)
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month').agg({
    'Revenue': 'sum',
    'Order_ID': 'count'
}).round(2)
monthly_sales.columns = ['Revenue', 'Orders']
print(monthly_sales.to_string())

print("\n8. CUSTOMER ANALYSIS")
print("-" * 80)
customer_stats = df.groupby('Customer_ID').agg({
    'Revenue': 'sum',
    'Order_ID': 'count',
    'Rating': 'mean'
}).round(2)
customer_stats.columns = ['Total_Spent', 'Orders', 'Avg_Rating']
customer_stats = customer_stats.sort_values('Total_Spent', ascending=False)
print(f"Unique Customers: {len(customer_stats)}")
print(f"Average Customer Value: Rs {customer_stats['Total_Spent'].mean():,.2f}")
print(f"Average Orders per Customer: {customer_stats['Orders'].mean():.2f}")
print("\nTop 5 Customers:")
print(customer_stats.head(5).to_string())

print("\n" + "="*80)
print("GENERATING VISUALIZATIONS...")
print("="*80 + "\n")

# Create visualizations
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 1. Revenue by Category
ax1 = fig.add_subplot(gs[0, 0])
category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
ax1.bar(category_revenue.index, category_revenue.values, color='steelblue', edgecolor='black')
ax1.set_title('Revenue by Category', fontweight='bold', fontsize=11)
ax1.set_ylabel('Revenue (Rs)')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', alpha=0.3)

# 2. Orders by Region
ax2 = fig.add_subplot(gs[0, 1])
region_orders = df['Region'].value_counts()
ax2.bar(region_orders.index, region_orders.values, color='coral', edgecolor='black')
ax2.set_title('Orders by Region', fontweight='bold', fontsize=11)
ax2.set_ylabel('Number of Orders')
ax2.grid(axis='y', alpha=0.3)

# 3. Revenue Distribution Pie
ax3 = fig.add_subplot(gs[0, 2])
ax3.pie(category_revenue.values, labels=category_revenue.index, autopct='%1.1f%%', startangle=90)
ax3.set_title('Revenue Distribution by Category', fontweight='bold', fontsize=11)

# 4. Monthly Revenue Trend
ax4 = fig.add_subplot(gs[1, 0])
monthly_rev = df.groupby('Month')['Revenue'].sum()
ax4.plot(range(len(monthly_rev)), monthly_rev.values, marker='o', linewidth=2.5, markersize=8, color='steelblue')
ax4.bar(range(len(monthly_rev)), monthly_rev.values, alpha=0.3, color='steelblue')
ax4.set_title('Monthly Revenue Trend', fontweight='bold', fontsize=11)
ax4.set_ylabel('Revenue (Rs)')
ax4.set_xticks(range(len(monthly_rev)))
ax4.set_xticklabels([str(m) for m in monthly_rev.index], rotation=45)
ax4.grid(axis='y', alpha=0.3)

# 5. Price Distribution
ax5 = fig.add_subplot(gs[1, 1])
ax5.hist(df['Price'], bins=15, color='lightgreen', edgecolor='black')
ax5.set_title('Price Distribution', fontweight='bold', fontsize=11)
ax5.set_xlabel('Price (Rs)')
ax5.set_ylabel('Frequency')
ax5.grid(axis='y', alpha=0.3)

# 6. Rating Distribution
ax6 = fig.add_subplot(gs[1, 2])
rating_counts = df['Rating'].value_counts().sort_index()
ax6.bar(rating_counts.index, rating_counts.values, color='gold', edgecolor='black', width=0.2)
ax6.set_title('Customer Rating Distribution', fontweight='bold', fontsize=11)
ax6.set_xlabel('Rating')
ax6.set_ylabel('Number of Orders')
ax6.set_xticks(rating_counts.index)
ax6.grid(axis='y', alpha=0.3)

# 7. Top 10 Products
ax7 = fig.add_subplot(gs[2, :2])
top_10_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=True).tail(10)
ax7.barh(range(len(top_10_products)), top_10_products.values, color='steelblue', edgecolor='black')
ax7.set_yticks(range(len(top_10_products)))
ax7.set_yticklabels(top_10_products.index, fontsize=9)
ax7.set_title('Top 10 Products by Revenue', fontweight='bold', fontsize=11)
ax7.set_xlabel('Revenue (Rs)')
ax7.grid(axis='x', alpha=0.3)

# 8. Customer Satisfaction vs Spending
ax8 = fig.add_subplot(gs[2, 2])
ax8.scatter(customer_stats['Total_Spent'], customer_stats['Avg_Rating'], 
           alpha=0.6, s=100, color='steelblue', edgecolor='black')
ax8.set_title('Satisfaction vs Spending', fontweight='bold', fontsize=11)
ax8.set_xlabel('Total Spent (Rs)')
ax8.set_ylabel('Average Rating')
ax8.grid(True, alpha=0.3)

plt.suptitle('E-Commerce Sales Dashboard', fontsize=16, fontweight='bold', y=0.995)
plt.show()

print("\nVISUALIZATIONS DISPLAYED SUCCESSFULLY!")

print("\n9. KEY INSIGHTS AND RECOMMENDATIONS")
print("-" * 80)
top_category = category_analysis.index[0]
top_region = region_analysis.index[0]
top_product = df.groupby('Product')['Revenue'].sum().idxmax()

print(f"Top Performing Category: {top_category}")
print(f"Top Performing Region: {top_region}")
print(f"Best Selling Product: {top_product}")
print(f"Average Profit Margin: {df['Profit_Margin'].mean():.2f}%")
print(f"Customer Retention Rate: {(customer_stats['Orders'] > 1).sum() / len(customer_stats) * 100:.1f}%")

print("\n" + "="*80)
print("ANALYSIS COMPLETE - ALL DATA AND CHARTS GENERATED")
print("="*80 + "\n")
