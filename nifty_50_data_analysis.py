import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("NIFTY_50_Data.csv")
print(df.head())
print(df.info())
print("/n/n")
df['Date'] = pd.to_datetime(df['Date'])

df['year'] = pd.DatetimeIndex(df['Date']).year
year_list = df['year'].unique()
print(year_list)
print("/n/n")

date_list = []
for i in year_list : 
    include = df[df["Date"].dt.year == i].min()
    date_list.append(include['Date'])
print(date_list)
print("/n/n")

close_list = []
for i in date_list :
    cl = df.where(df["Date"] == i)
    cl = (cl.dropna())
    close_list.append(cl['Close'].values[0])

close_list.reverse()

ret_list = []
for i in range(len(close_list)-5) :
    ret = close_list[i+5] - close_list[i]
    perc = (ret/close_list[i])*100
    ret_list.append(perc)
year_list = list(year_list)
year_list.reverse()
print(ret_list)

for i in range(len(year_list)-5):
    print(year_list[i], "-", year_list[i+5], ret_list[i])

return_list = []
for i in range(len(ret_list)):
    returns = (ret_list[i] * 50000)/100
    return_list.append(returns)
    print(year_list[i], "-", year_list[i+5],"---", ret_list[i], "===", return_list[i])

total = 0
for i in range(0, len(return_list)):
    total += return_list[i]
print("Total : ",total)

years = []
for i in range(len(year_list)-5):
    year = f"{year_list[i]}-{year_list[i+5]}"
    years.append(year)

plt.figure(figsize = (10, 5))
plt.plot(years, ret_list, color = 'Blue', linestyle = "--")
plt.xlabel("5-Year Periods")
plt.ylabel("Return(%)")
plt.title("NIFTY 50 - 5 Years Returns Over Time")
plt.show()
