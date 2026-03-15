import pandas as pd 
df=pd.read_csv("data/online_gaming_behavior_dataset.csv")
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nEngagement Distribution:")
print(df['EngagementLevel'].value_counts())