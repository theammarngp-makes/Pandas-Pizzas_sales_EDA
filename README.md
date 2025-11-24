# 🍕 Pandas Pizza Sales EDA

## A complete Exploratory Data Analysis (EDA) project where I analyzed 48,000+ pizza orders using Pandas, extracted business insights, and prepared clean visual summaries.
## Project Overview
  This project explores a pizza company’s sales dataset consisting of:
	•	orders.csv
	•	order_details.csv
	•	pizzas.csv
	•	pizza_types.csv

The dataset includes order timestamps, quantities, pizza categories, sizes, and pricing.
Using Python (Pandas), I performed data cleaning and analysis to find trends, revenue patterns, and customer preferences.

## Objectives
 •	Clean and preprocess raw CSV files
 •	Extract date/time features
 •	Join relational tables
 •	Calculate revenue, quantity trends, and top-selling pizzas
 •	Analyse sales by:
 •	Day of the week
 •	Hour of the day
 •	Pizza category
 •	Pizza size
 •	Individual pizzas
 •	Generate actionable insights

 ## Techniques Used
  •	merge, groupby, agg
  •	sort_values, value_counts
	•	dt.date, dt.hour, dt.weekday
	•	Feature engineering
	•	Revenue calculation
	•	Time-based EDA
	
# Insights
## Q1.Retrive the total no of orders placed 
```
Total order placed = 48620
```
## Q2.Claculate total revenue from pizza sales
```
Total revenue from pizza sales = 817860.0499999999$
```
## Q3.Identify highest price of pizza
```
Highest price of pizza = 35.95
```
## Q4.Identify most common pizza size 
```
Most common pizza size = XXL
```

## Q5.List top 5 most order pizzas with quantity
### Top 5 most ordered pizzas:
```
name
The Classic Deluxe Pizza      2453
The Barbecue Chicken Pizza    2432
The Hawaiian Pizza            2422
The Pepperoni Pizza           2418
The Thai Chicken Pizza        2371
Name: quantity, dtype: int64
```

## Q6.Find total quantity of each pizza ordered 
```
name
The Classic Deluxe Pizza                      2453
The Barbecue Chicken Pizza                    2432
The Hawaiian Pizza                            2422
The Pepperoni Pizza                           2418
The Thai Chicken Pizza                        2371
The California Chicken Pizza                  2370
The Sicilian Pizza                            1938
The Spicy Italian Pizza                       1924
The Southwest Chicken Pizza                   1917
The Big Meat Pizza                            1914
The Four Cheese Pizza                         1902
The Italian Supreme Pizza                     1884
The Vegetables + Vegetables Pizza             1526
The Mexicana Pizza                            1484
The Napolitana Pizza                          1464
The Prosciutto and Arugula Pizza              1457
The Spinach and Feta Pizza                    1446
The Pepper Salami Pizza                       1446
The Italian Capocollo Pizza                   1438
The Greek Pizza                               1420
The Five Cheese Pizza                         1409
The Pepperoni, Mushroom, and Peppers Pizza    1359
The Green Garden Pizza                         997
The Chicken Alfredo Pizza                      987
The Italian Vegetables Pizza                   981
The Chicken Pesto Pizza                        973
The Spinach Pesto Pizza                        970
The Soppressata Pizza                          961
The Spinach Supreme Pizza                      950
The Calabrese Pizza                            937
The Mediterranean Pizza                        934
The Brie Carre Pizza                           490
Name: quantity, dtype: int64
```
## Q7.Determine the disrtibution of orders by hrs of the day
```
hrs
12    6543
13    6203
18    5359
17    5143
19    4350
16    4185
14    3521
20    3487
15    3170
11    2672
21    2528
22    1370
23      68
10      17
9        4
Name: order_id, dtype: int64
```

## Q8.JOIN relevent table to find the category wise ditribution of pizzas 
```category
Chicken    23.955138
Classic    26.905960
Supreme    25.456311
Veggie     23.682591
Name: Total, dtype: float64
```

## Q9.Group the orders by date and calculate the average number of pizzas ordered per day
```
138.47486033519553
```

## Q10.Identify the day of the week with highest number of orders
```
weekday
Friday       16.786812
Monday       16.851868
Saturday     16.748117
Sunday       16.765844
Thursday     16.868565
Tuesday      16.901199
Wednesday    16.832191
Name: Total, dtype: float64
```

## Q11.Calculate the percentage contribution of each pizza type to total revenue
```
category
Chicken    23.955138
Classic    26.905960
Supreme    25.456311
Veggie     23.682591
```

## Q12.Analyze the cumulative revenue generated over time
```
time
2025-11-24 09:52:21        83.00
2025-11-24 10:25:19        95.50
2025-11-24 10:34:34       148.75
2025-11-24 10:43:04       201.50
2025-11-24 10:50:46       251.75
                         ...    
2025-11-24 23:05:08    817700.05
2025-11-24 23:05:16    817726.05
2025-11-24 23:05:17    817766.05
2025-11-24 23:05:24    817827.55
2025-11-24 23:05:52    817860.05
```

 ## Q13.Determine the top 3 most ordered pizza types based on revenue for each pizza category.
```
	category                                        name     Total
5   Chicken                      The Thai Chicken Pizza  43434.25
4   Chicken                 The Southwest Chicken Pizza  34705.75
3   Chicken                     The Chicken Pesto Pizza  16701.75
13  Classic  The Pepperoni, Mushroom, and Peppers Pizza  18834.50
12  Classic                         The Pepperoni Pizza  30161.75
11  Classic                        The Napolitana Pizza  24087.00
22  Supreme                   The Spinach Supreme Pizza  15277.75
21  Supreme                     The Spicy Italian Pizza  34831.25
20  Supreme                       The Soppressata Pizza  16425.75
31   Veggie           The Vegetables + Vegetables Pizza  24374.75
30   Veggie                  The Spinach and Feta Pizza  23271.25
29   Veggie                     The Spinach Pesto Pizza  15596.00
```

  
Mohammad Ammar
Aspirant Data Scientist | ENTC Engineer
Focused on real-world data analysis and building a strong portfolio.
