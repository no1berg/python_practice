### Based on https://pandas.pydata.org/docs/user_guide/10min.html
import numpy as np
import pandas as pd


# Creating a Series by passing a list of values,
# letting pandas create a default RangeIndex
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s


# |%%--%%| <MbbgxRzlGk|BzPDAfcPuP>

# Creating a DataFrame by passing a NumPy array with,
# a datetime index using date_range() and labeled columns::
dates = pd.date_range("20130101", periods=6)

dates
# |%%--%%| <BzPDAfcPuP|NhfI8PZZeJ>

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df


# |%%--%%| <NhfI8PZZeJ|Ywd0MDnBpb>

# Creating a DataFrame by passing a dictionary of objects where,
# the keys are the column labels and the values are the colum values
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
df2
# |%%--%%| <Ywd0MDnBpb|CAKN6giK4K>

# The columns of the resulting DataFrame have different dtypes
df2.dtypes
# |%%--%%| <CAKN6giK4K|OzZVsDcee3>

# Use DataFrame.head() and DataFrame.tail() to view the top and bottom
# frame respectively

df.head()
df.tail()
# |%%--%%| <OzZVsDcee3|DHPjG8BGf8>

# Display the DataFrame.index
df.index
# |%%--%%| <DHPjG8BGf8|qRccPMItVS>

# Display the DataFrame.columns
df.columns


# |%%--%%| <qRccPMItVS|d34wXlbkcq>

# Return a NumPy representation of the underlying data with
# DataFrame.to_numpy() without the index or column labels
df.to_numpy()

# |%%--%%| <d34wXlbkcq|CRI3Sj5MTx>

# Show a quick statistic summary of the data using describe()
df.describe()


# |%%--%%| <CRI3Sj5MTx|Noeqa0kqOw>

# Transpose the data using DataFrame.T
df.T

# |%%--%%| <Noeqa0kqOw|5tmuK80jcj>

# Sort by an axis using DataFrame.sort_index()
df.sort_index(axis=1, ascending=False)

# |%%--%%| <5tmuK80jcj|O2HiXplWr8>

# Sort by values using DataFrame.sort_values()
df.sort_values(by="B")
# |%%--%%| <O2HiXplWr8|fwtpvPtOLE>

### Selection

## Getitem([])

# For a DataFrame, passing a single label selects a column and yields a
# Series equivalent to df.A
df["A"]


# |%%--%%| <fwtpvPtOLE|RmG4zukLRX>

# For a DataFrame, passing a slice ':' selects matching rows
df[0:3]

df["20130101":"20130104"]

# |%%--%%| <RmG4zukLRX|GH09jrraia>

## Selection by label

# Selecting a row matching a label
df.loc[dates[0]]

# |%%--%%| <GH09jrraia|CQnieuQe4T>

# Select all rows (':') with a select column labels
df.loc[:, ["A", "B"]]

# |%%--%%| <CQnieuQe4T|OD7tbKDsZi>

# For label slicing, both endpoints are included:
df.loc["20130102":"20130104", ["A", "B"]]

# |%%--%%| <OD7tbKDsZi|lO2EJvmApY>

# Selecting a single row and column label returns a scalar:
df.loc[dates[0], "A"]

# |%%--%%| <lO2EJvmApY|s3BDvJFDoU>

# For getting fast access to a scalar (equivalent to the prior method)
df.at[dates[0], "A"]

# |%%--%%| <s3BDvJFDoU|siEJlDgdqb>

## Selection by position

# Select via the position of the passed integers:
df.iloc[3]

# |%%--%%| <siEJlDgdqb|EMcJiouisW>

# Integer slices act similar to NumPy/Python
df.iloc[3:5, 0:2]

# |%%--%%| <EMcJiouisW|Zn7wHdCdt8>

# Lists of integer position locations:
df.iloc[[1, 2, 4], [0, 2]]


# |%%--%%| <Zn7wHdCdt8|RGpmN5SjmP>

# For slicing rows explicitly
df.iloc[1:3, :]

# |%%--%%| <RGpmN5SjmP|uEGqUqHTyT>

# For slicing columns explicitly:
df.iloc[:, 1:3]

# |%%--%%| <uEGqUqHTyT|j51QEHZYFG>

# For getting a value explicitly:
df.iloc[1, 1]

# |%%--%%| <j51QEHZYFG|NsN0evr5R6>

# For getting fast access to a scalar (equivalent to the prior method)
df.iat[1, 1]

# |%%--%%| <NsN0evr5R6|3llKaVg7Mg>

## Boolean indexing

# Select rows where df.A is greater than 0
df[df["A"] > 0]
# |%%--%%| <3llKaVg7Mg|I4LeoIiszY>

# Selecting values from a DataFrame where boolean condition is met
df[df > 0]

# |%%--%%| <I4LeoIiszY|IVGJdeKW0q>

# Using isin() method for filtering
df2.copy()

df2["E"] = ["one", "one", "two", "three"]
df2

df2[df2["E"].isin(["two", "four"])]

# |%%--%%| <IVGJdeKW0q|Ntj0g4PPwd>

## Setting

# Setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1

df["F"] = s1
df

# |%%--%%| <Ntj0g4PPwd|NcMp1J4YII>

# Setting values by label:
df.at[dates[0], "A"] = 0

# |%%--%%| <NcMp1J4YII|HNzXgIVf1E>

# Setting values by position:
df.iat[0, 1] = 0

# |%%--%%| <HNzXgIVf1E|cOVG1DUzaD>

# The results of the prior setting operations:
df

# |%%--%%| <cOVG1DUzaD|6Tsvpqu7Mi>

# A 'Where' operation with setting:
df2 = df.copy()

df2[df2 > 0] = -df2

df2

# |%%--%%| <6Tsvpqu7Mi|zQ6ThPnLce>

### Missing data

# For NumPy data types, np.nan represents missing data. It is be default
# not included in computations

# Reindexing allows you to change/add/delete the index on a specific axis
# This returns a copy of the data:
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
df1
# |%%--%%| <zQ6ThPnLce|ii9XHub2zK>

# DataFrame.dropna() drops any rows that have missing data:
df1.dropna(how="any")

# |%%--%%| <ii9XHub2zK|l1akH1eFgh>

# DataFrame.fillna() fills missing data:
df1.fillna(value=5)

# |%%--%%| <l1akH1eFgh|gMJQ3L6lbk>

# isna() gets the boolean mask where values are nan:
pd.isna(df1)

# |%%--%%| <gMJQ3L6lbk|IbXO3phvVw>

### Operations

## Stats

# Operations in general 'exclude' missing data

# Calculate the mean value for each column:
df.mean()

# |%%--%%| <IbXO3phvVw|2TWYfB53ju>

# Calculate the mean value for each row:
df.mean(axis=1)

# |%%--%%| <2TWYfB53ju|pen3yRt88e>

# Operating with another Series or DataFrame with a different index or
# column will align the result with the union of the index or columnn labels
# In addition, pandas automatically broadcasts along the specified
# dimension and will fill unaligned labels with np.nan
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s

df.sub(s, axis="index")
# |%%--%%| <pen3yRt88e|4twCUSf8uO>

## User defined functions

# DataFrame.agg() and DataFrame.transform() applies a user defined function
# that reduces or broadcasts its return respectively
df.agg(lambda x: np.mean(x) * 5.6)

df.transform(lambda x: x * 101.2)


# |%%--%%| <4twCUSf8uO|48O7j3P2Qs>

## Value counts

s = pd.Series(np.random.randint(0, 7, size=10))
s

s.value_counts()

# |%%--%%| <48O7j3P2Qs|mUqF7ljI35>

## String methods

# Series is equipped with a set of string processing methods in the str
# attribute that make it easy to operate on each element of the array,
# as in the code snippet below
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower()

# |%%--%%| <mUqF7ljI35|Y6775msqoq>

### Merge

## Concat

# Pandas provides various facilities for easily combining together Series,
# and DataFrame objects with various kinds of logic for the indexes and
# and relational algebra functionality in the case of join/merge-type operations

# Concatenating pandas objects together row-wise with concat()
df = pd.DataFrame(np.random.randn(10, 4))
df

# Break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
# |%%--%%| <Y6775msqoq|gpXpYsbG6I>

## Join

# merge() enables SQL style join types along specific columns:
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

print(left)
print(right)

pd.merge(left, right, on="key")

# |%%--%%| <gpXpYsbG6I|tz5XJGNx6w>

# merge() on unique keys:
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

print(left)
print(right)

pd.merge(left, right, on="key")

# |%%--%%| <tz5XJGNx6w|EoCrA7YMLH>

### Grouping

# By 'group by' we are referring to a process involving one or more
# of the following steps

#       * Splitting the data into groups based on some criteria
#       * Applying a function to each group independently
#       * Combining the results into a data structure

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

df
# |%%--%%| <EoCrA7YMLH|KMXgk2Ltq8>

# Grouping by a column label, selecting column labels, and then applying the
# DataFrameGroupBy.sum() function to the resulting groups

df.groupby("A")[["C", "D"]].sum()

# |%%--%%| <KMXgk2Ltq8|V0Dt3hdy30>

# Grouping by multiple columns label MultiIndex
df.groupby(["A", "B"]).sum()

# |%%--%%| <V0Dt3hdy30|XRfeN4bE6j>

### Reshaping

## Stack

arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]

index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]
df2

# |%%--%%| <XRfeN4bE6j|1P9JVtmnqo>

# The stack() method "compresses" a level in the DataFrame's columns
stacked = df2.stack(future_stack=True)
stacked

# |%%--%%| <1P9JVtmnqo|kQYhE5ohXn>

# With a 'stacked' DataFrame or Series (having a MultiIndex as the index),
# the inverse operation of stack() is unstack(), which by default
# unstacks the last level:
stacked.unstack()  # Last level
stacked.unstack(1)
stacked.unstack(0)


# |%%--%%| <kQYhE5ohXn|iB1HJAlnWT>

## Pivot tables

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

df

# |%%--%%| <iB1HJAlnWT|pGzOntLHmA>

# pivot_table() pivots a DataFrame specifying the values, index, and columns
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])

# |%%--%%| <pGzOntLHmA|geLqXv87SC>

### Time series

# pandas has simple, powerful, and efficient functionality for performing
# operations during frequency conversion (e.g., converting secondly data into
# 5-minutely data). This is extremely common in, but not limited to,
# financial applications
rng = pd.date_range("1/1/2012", periods=100, freq="s")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts.resample("5Min").sum()
# |%%--%%| <geLqXv87SC|aXzhqBocCJ>

# Series.tz_localize() localizes a time series into a time zone
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

ts = pd.Series(np.random.randn(len(rng)), rng)
ts

ts_utc = ts.tz_localize("UTC")
ts_utc

# |%%--%%| <aXzhqBocCJ|cOH8sgYEBT>

# Series.tz_convert() converts a time zone aware time series into another
# time zone
ts_utc.tz_convert("US/Eastern")

# |%%--%%| <cOH8sgYEBT|L5dPlZC7Xw>

# Adding a non-fixed duration (BusinessDay) to a time series
rng
rng + pd.offsets.BusinessDay(5)

# |%%--%%| <L5dPlZC7Xw|a2JntdneeI>

### Categoricals

# Pandas can include categorical data in a DataFrame
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

# |%%--%%| <a2JntdneeI|x2oH8qy3Mz>

# Converting the raw grades to a categorical data type
df["grade"] = df["raw_grade"].astype("category")
df["grade"]

# |%%--%%| <x2oH8qy3Mz|cMKA1l0Fub>

# Rename the categories to more meaningful names
new_categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.rename_categories(new_categories)
df["grade"]
# |%%--%%| <cMKA1l0Fub|lP0fXSMRI8>

# Reorder the categories and simultaneously add the missing categories
# (methods under Series.cat() return a new Series by default)
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
df["grade"]

# |%%--%%| <lP0fXSMRI8|RU6AiKRtsF>

# Sorting is per order in the categories, not lexical order
df.sort_values(by="grade")

# |%%--%%| <RU6AiKRtsF|WxGIbn3xbq>

# Grouping by a categorical column with observed=False also
# shows empty categories
df.groupby("grade", observed=False).size()

# |%%--%%| <WxGIbn3xbq|vaoN1WNv52>

### Plotting

# Using the standard convention for referencing the matplotlib API:
import matplotlib.pyplot as plt

plt.close("all")

# the plt.close method is used to close a figure window

# |%%--%%| <vaoN1WNv52|Ti3woCaOdi>

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

ts.plot()
# |%%--%%| <Ti3woCaOdi|Kb6fIhq0xB>

# plot() plots all columns:
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)


df = df.cumsum()

plt.figure()
df.plot()
plt.legend(loc="best")
# |%%--%%| <Kb6fIhq0xB|sJJVTMk2Es>

### Importing and Exporting data

## CSV

# Writing to a csv file: using DataFrame.to:csv()
df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
df.to_csv("foo.csv")


# |%%--%%| <sJJVTMk2Es|SC2RQuHuCm>

# Reading from a csv file: using read_csv()
pd.read_csv("foo.csv")

# |%%--%%| <SC2RQuHuCm|JQ1k5axHwe>

## Parquet

# Writing to a Parquet file:
df.to_parquet("foo.parquet")

# |%%--%%| <JQ1k5axHwe|tgt6nuRTHe>

# Reading from a Parquet file:
pd.read_parquet("foo.parquet")
# |%%--%%| <tgt6nuRTHe|CEE8fWJZWq>

## Excel

# Writing to an excel file:
df.to_excel("foo.xlsx", sheet_name="Sheet1")

# |%%--%%| <CEE8fWJZWq|6UsNUAZ7lg>

# Reading from an excel file:
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
