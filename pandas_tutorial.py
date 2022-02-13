from statistics import mean
import pandas as pd

dataset_dict = {
    "key1" : [1, 2, 3],
    "key2" : [23, 4, 5]
}
dataframe = pd.DataFrame(dataset_dict)

series_list = [1, 6, 7]
series = pd.Series(series_list, index=["x", "y", "z"])
# print(series["y"])
# print(series.to_string())

series_dict = {"x" : 2, "y": 3, "z": 4}
series = pd.Series(series_dict)
# print(series)


dataframe = pd.DataFrame(dataset_dict, index=["day1","day2","day3"])
# print(dataframe)
# print(dataframe.loc["day1"])
# print(dataframe.head())
# print(dataframe.tail())
# print(dataframe["key1"])



df = pd.read_csv("datasets/dirtydata.csv")

# ============ Cleaning =============

# remove nulls
median = df["Calories"].median()
most_frequent = df["Calories"].mode()
mean = df["Calories"].mean()

df["Calories"].fillna(median, inplace=True)

# wrong date format
df["Date"] = pd.to_datetime(df["Date"])
df.dropna(subset=["Date"],inplace=True)


# a function to check for range of anything
print(df.index)

for i in df.index:
    if df["Duration"].loc[i] > 100:
        df.drop(i, inplace=True) # remove it
        # df["Duration"].loc[i] = 500 # or edit it

# Drop dupplicates (complete rows dupplicates)
df.drop_duplicates(inplace=True)


# ============ Correlation =============
corr_matrix = df.corr()
print(corr_matrix)
'''
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.001616  0.043032 -0.127442
Pulse    -0.001616  1.000000  0.261426  0.478723
Maxpulse  0.043032  0.261426  1.000000  0.329600
Calories -0.127442  0.478723  0.329600  1.000000

1 means perfect relation, any value > 0.6 (or < -0.6)
means good relation (if +ve means it directly propostional if -ve reverse propotional),
small values means no relation between columns
'''

print(df.to_string())

# ============ Visualization =============
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/data.csv")

# Scatter | Histogram plotting (scatter | hist)
# df.plot(kind="scatter", x = "Duration", y = "Pulse")
# df["Duration"].plot(kind="hist")

# create different subplot for each colum(series) in the data frame
# df.plot(subplots=True)

# Plot every colum (values at each index)
df.plot()
plt.show()