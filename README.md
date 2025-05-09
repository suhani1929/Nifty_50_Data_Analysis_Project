# 📈 NIFTY 50 Data Analysis
## 🗂️ Project Overview
This project analyzes historical NIFTY 50 stock index data to calculate 5-year returns and simulate the growth of a ₹50,000 investment over time. The analysis helps visualize long-term trends in the Indian stock market and can support better investment decision-making.

## ✅ Objectives
- Track the performance of NIFTY 50 over multiple 5-year periods.

- Simulate investment growth using actual market data.

- Visualize market trends and returns through a line graph.

- Identify market growth or slowdown periods to guide investors.

## 📊 Dataset
- File: `NIFTY_50_Data.csv`

- Columns:

     - Date – Trading date

     - Open – Opening price

     - High – Highest price of the day

     - Low – Lowest price of the day

     - Close – Closing price

## 🛠️ Tools & Libraries
- Language: Python

- Libraries:

     - pandas – For data processing

     - matplotlib – For visualization

- IDE: Visual Studio Code (recommended)

## 📌 Methodology
- Data Preprocessing

     - Load and clean the dataset

     - Convert Date column to datetime format

     - Identify the earliest trading day of each year
 
- 5-Year Return Calculation

     - Get closing prices from earliest trading days

     - Calculate percentage returns for each 5-year period

     - Simulate investment of ₹50,000 over each period

- Visualization

     - Plot a line chart showing 5-year return trends

## 📉 Sample Output
- Printed returns for each 5-year window.

- Calculated profit/loss on ₹50,000 investment.

- A line graph visualizing the return trends.

## 🧩 Challenges & Solutions
- Missing Data: Used earliest available trading day when the exact first day was missing.

- Data Cleaning: Converted dates and removed nulls using .dropna().

- Accurate Calculations: Verified close prices and return logic for consistency.

## 📌 Results
- Clear trend of NIFTY 50 growth over multiple periods.

- Visual proof of long-term investment value.

- Total return calculation for ₹50,000 investment.

## 📚 Key Learnings
- Long-term investing in the NIFTY 50 can yield strong returns if done patiently.

- Markets fluctuate, but long-term trends show growth.

- Investment timing and patience are critical.
