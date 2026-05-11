import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sys

# Redirect all print output to a text file
sys.stdout = open('analysis_output.txt', 'w')

df = pd.read_csv(r"D:\KUNAL\Python\tips.csv")

#--------------over all structure of dataset---------------
headings = df.columns
description = df.describe()
structure = df.shape
data_type = df.dtypes

print(f"headings of datasets \n{headings}")
print(f"\ndescription of all over dataset \n{description}")
print(f"\nStructure of dataset \n{structure} (Rows X Column)")
#--------------------Data Cleaning-------------------------
#Remove duplicates rows
df = df.drop_duplicates()

#check missing values present in dataset
df.isnull().sum()
print(f"\nMissing values in dataset \n{df.isnull().sum()}")

#filling with most frequent value ex:- day, time, size and sex(Male/Female)
df["day"] = df["day"].fillna(df["day"].mode()[0])
df["sex"] = df["sex"].fillna(df["sex"].mode()[0])
df["size"] = df["size"].fillna(df["size"].mode()[0])
df["time"] = df["time"].fillna(df["time"].mode()[0])

print(f"\ninformation with data types of dataset \n{data_type}")

#if information is important then fill missing values. else remove rows, columns with any missing value.

#filling values with median ex:- tip and total_bill (already done above for others)
df["tip"] = df["tip"].fillna(df["tip"].median())
df["total_bill"] = df["total_bill"].fillna(df["total_bill"].median())

print(f"\nMissing values filling successfully")
print(f"\nData Cleaning Successfully Completed")

#check any missing values present in dataset
df.isnull().sum()
print(f"\nMissing values in dataset \n{df.isnull().sum()}")

#it shows average and total income of each day
income = df.groupby("day").agg({
    "tip" : ["mean","sum"],
    "total_bill" : ["mean","sum"]
})
print(f"\nIncome by day \n{income}")

#---------------------Visualization----------------------
sns.set_theme(style = "whitegrid")

# Simple Bar plot (Daily Revenue)
sns.barplot(x="day", y="total_bill", data=df, estimator=sum)  # Sum total_bill per day
plt.title("Daily Revenue")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.savefig("daily_revenue.png")
plt.show()

#scatter plot(Tipper Relationship)
sns.scatterplot(
    x = "total_bill",
    y = "tip",
    hue = "time",
    data = df
)
plt.savefig("tip_relationship.png")
plt.show()

#box plot(display quartiles, median and outliers)
sns.boxplot(
    x = "day",
    y = "tip",
    data = df
)
plt.savefig("tip_by_day.png")
plt.show()

#heatmap(correlation metrics)
corr = df.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot = True, #show values
    cmap = "coolwarm", #color scheme
    vmin = -1, vmax = 1, #value range
    square = True #square cells
)
plt.savefig("correlation_heatmap.png")
plt.show()
print(f"\nVisualization Successfully Completed")
