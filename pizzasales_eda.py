import pandas as pd

pizza_types = pd.read_csv("/Users/mohammadammar/Desktop/SQL_pizza_sales/pizza_sales/pizza_types.csv")
pizzas = pd.read_csv("/Users/mohammadammar/Desktop/SQL_pizza_sales/pizza_sales/pizzas.csv")
orders = pd.read_csv("/Users/mohammadammar/Desktop/SQL_pizza_sales/pizza_sales/orders.csv")
order_details = pd.read_csv("/Users/mohammadammar/Desktop/SQL_pizza_sales/pizza_sales/order_details.csv")

# Merging all the tables 
order = orders.merge(order_details,on="order_id",how="left")
order = order.merge(pizzas,on="pizza_id",how="left")
order = order.merge(pizza_types,on="pizza_type_id",how="left")
order.drop(columns=["ingredients"],inplace=True)
# order.drop(columns=["order_details_id"],inplace=True)
# order.drop(columns=["order_id"],inplace=True)
order["Total"] = order["quantity"]*order["price"]
order["date"] = pd.to_datetime(order["date"])
order["month"] = order["date"].dt.month_name()
order["date"] = pd.to_datetime(order["date"])
order["weekday"] = order["date"].dt.day_name()
order["Tax"] = order["Total"]*1.1

# 1.Retrive the total no of orders placed
print(f"Total order placed = {order["order_id"].count()}")
# 2.Claculate total revenue from pizza sales
print(f"Total revenue from pizza sales = {order["Total"].sum()}$")
# 3.Identify highest price of pizza
print(f"Highest price of pizza = {order['price'].max()}")
# 4.Identify most common pizza size 
print(f"Most common pizza size = {order['size'].max()}")
# 5.List top 5 most order pizzas with quantity
top5 = order.groupby("name")["quantity"].sum().sort_values(ascending=False).head()
print("Top 5 most ordered pizzas:")
print(top5)

# 1.Find total quantity of each pizza ordered 
total_qty = order.groupby("name")["quantity"].sum().sort_values(ascending=False)
print(total_qty)
# 2.Determine the disrtibution of orders by hrs of the day
order["time"] = pd.to_datetime(order["time"])
order["hrs"] = order["time"].dt.hour
grp = order.groupby("hrs")["order_id"].count().sort_values(ascending=False)
print(grp)
# 3.JOIN relevent table to find the category wise ditribution of pizzas 
ct = order.groupby("category")["quantity"].sum().sort_values(ascending=False)
print(ct)
# 4.Group the orders by date and calculate the average number of pizzas ordered per day
dc = order.groupby("date")["quantity"].sum().mean()
print(dc)
# 5.Identify the day of the week with highest number of orders
wk= order.groupby("weekday")["order_id"].count().sort_values(ascending=False)
print(wk)
wkq= order.groupby("weekday")["quantity"].sum().sort_values(ascending=False)
print(wkq)

# 1.Calculate the percentage contribution of each pizza type to total revenue.
ct = order.groupby("category")["Total"].sum()/order["Total"].sum()*100
print(ct)

# 2.Analyze the cumulative revenue generated over time
dail=order.groupby("time")["Total"].sum().sort_index()
cumv = dail.cumsum()
print(cumv)

# 3.Determine the top 3 most ordered pizza types based on revenue for each pizza category.
pt = order.groupby(["category","name"])["Total"].sum().reset_index().sort_values(["category","name"],ascending=[True,False]).groupby("category").head(3)
fgrp=order.groupby("weekday")["Total"].mean()
print(fgrp)