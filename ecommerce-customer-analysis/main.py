import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/ecommerce_data.csv")

# Display the first 5 rows
print("First 5 rows:")
print(df.head(5))

# Basic Info
print("\n Dataset Info:")
print(df.info())

# Summary Statistics
print("\n Summary Statistics:")
print(df.describe())

print("\n Top Revenue generating countries: ")
revenue_by_country = df.groupby('Country')['PurchaseAmount'].sum().sort_values(ascending=False)
print(revenue_by_country)

revenue_by_country.plot(kind="bar", color='skyblue')
plt.title('Revenue by country')
plt.xlabel('country')
plt.ylabel('Total Purchase Amount')
plt.tight_layout()
plt.show()

# # Top-spending customers
# top_customers = df.groupby('CustomerID')['PurchaseAmount'].sum().sort_values(ascending=True)
# print("Displaying Top Five customers")
# print(top_customers.head(5))
# top_5_customers = top_customers.head(5)

# #ploting top spending customers
# top_5_customers.plot(kind='barh', color='orange')
# plt.title('Top 5 Spending Customers')
# plt.xlabel('Total Purchase Amount')
# plt.ylabel('Customer ID')
# plt.tight_layout()
# plt.show()

# Top-spending customers (corrected to show highest spenders)
top_customers = df.groupby('CustomerID')['PurchaseAmount'].sum().sort_values(ascending=False)
print("Displaying Top Five Customers by Revenue:")
print(top_customers.head(5))

# Plot horizontal bar chart
top_5_customers = top_customers.head(5)
top_5_customers.plot(kind='barh', color='orange')
plt.title('Top 5 Spending Customers')
plt.xlabel('Total Purchase Amount')
plt.ylabel('Customer ID')
plt.tight_layout()
plt.show()


# Average purchase amount by gender:
avg_by_gender = df.groupby('Gender')['PurchaseAmount'].mean()
print("Displaying Top 5 Average purchase amount by gender")
print(avg_by_gender.head(5))

# Plot average purchase amount by gender (Pie Chart)
avg_by_gender.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Average Purchase Amount by Gender')
plt.axis('equal')  # Removes default y-label
plt.tight_layout()
plt.show()
