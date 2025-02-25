import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)
print("First 5 rows of the dataset:")
print(data.head())
print("\nDataset Info:")
print(data.info())
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)  
data.drop_duplicates(inplace=True)
print("\nStatistical Summary:")
print(data.describe())
survival_rate = data['Survived'].value_counts(normalize=True) * 100
print("\nSurvival Rate (%):")
print(survival_rate)
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', hue='Sex', data=data, palette='viridis')
plt.title("Survival Count by Gender")
plt.show()
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], kde=True, bins=30, color='blue')
plt.title("Age Distribution")
plt.show()
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=data, palette='coolwarm')
plt.title("Survival by Passenger Class")
plt.show()
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
