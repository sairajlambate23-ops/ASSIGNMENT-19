# # Q2

# import pandas as pd

#  # Load Dataset
# df = pd.read_csv("insurance - insurance.csv")

#  # First 10 Rows
# print("First 10 Rows:")
# print(df.head(10))

# Q3
# import pandas as pd

# # Load dataset
# df = pd.read_csv("insurance - insurance.csv")

# # Missing Values
# print("Missing Values:")
# print(df.isnull().sum())

# # Missing Value Percentage
# print("\nMissing Value Percentage:")
# print((df.isnull().sum() / len(df)) * 100)

# # Handle Missing Values
# df = df.dropna()

# # Check Duplicates
# duplicates = df.duplicated().sum()
# print("\nDuplicate Rows:", duplicates)

# # Remove Duplicates
# df = df.drop_duplicates()

# print("\nDataset Shape After Cleaning:", df.shape)

# # Q4


# import pandas as pd

# df = pd.read_csv("insurance - insurance.csv")

# # Statistical Summary
# print(df.describe())

# # Target Variable = expenses
# print("\nMinimum Expenses:", df['expenses'].min())
# print("Maximum Expenses:", df['expenses'].max())
# print("Mean Expenses:", df['expenses'].mean())
# print("Median Expenses:", df['expenses'].median())

# Q5

# import pandas as pd
# import matplotlib.pyplot as plt

# # Load Dataset
# df = pd.read_csv("insurance - insurance.csv")

# # Numeric Columns
# numeric_cols = ['age', 'bmi', 'children', 'expenses']

# # Histograms
# for col in numeric_cols:
#     plt.figure(figsize=(6,4))
#     plt.hist(df[col], bins=20)
#     plt.title(f'Histogram of {col}')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.grid(True)
#     plt.show()

# Q6

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv("insurance - insurance.csv")

# cat_cols = ['sex', 'smoker', 'region']

# for col in cat_cols:
#     plt.figure(figsize=(6,4))
#     sns.countplot(x=col, data=df)
#     plt.title(f'Count Plot of {col}')
#     plt.show()

# Q7

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load Dataset
# df = pd.read_csv("insurance - insurance.csv")

# # Select Numeric Columns
# numeric_df = df[['age', 'bmi', 'children', 'expenses']]

# # Correlation Heatmap
# plt.figure(figsize=(8,6))
# sns.heatmap(
#     numeric_df.corr(),
#     annot=True,
#     cmap='coolwarm',
#     fmt='.2f'
# )

# plt.title("Correlation Heatmap")
# plt.show()

# Q8
# import pandas as pd

# # Load Dataset
# df = pd.read_csv("insurance - insurance.csv")

# # Independent Features (X)
# X = df[['age', 'bmi', 'children']]

# # Dependent Feature (y)
# y = df['expenses']

# print("Independent Features (X):")
# print(X.head())

# print("\nDependent Feature (y):")
# print(y.head())

# Q9

# import pandas as pd

# # Load Dataset
# df = pd.read_csv("insurance - insurance.csv")

# # Check for categorical columns
# cat_cols = df.select_dtypes(include=['object']).columns

# print("Categorical Columns:")
# print(list(cat_cols))

# if len(cat_cols) == 0:
#     print("\nNo categorical columns found in the dataset.")
#     print("Encoding is not required.")
# else:
#     df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

#     print("\nDataset After Encoding:")
#     print(df_encoded.head())

# Q10

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load Dataset
df = pd.read_csv("insurance - insurance.csv")

# Independent Features
X = df[['age', 'bmi', 'children']]

# Apply Standard Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert to DataFrame
scaled_df = pd.DataFrame(
    X_scaled,
    columns=['age', 'bmi', 'children']
)

# Show First 5 Rows
print("First 5 Rows of Scaled Features:")
print(scaled_df.head())