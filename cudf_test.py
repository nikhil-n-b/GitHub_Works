# Import necessary libraries
import cudf
import pandas as pd

# Step 1: Load CSV file into cuDF DataFrame
# Assuming the CSV file is named 'customer_transactions.csv' and is located in the same directory as this script
file_path = 'customer_transactions.csv'
df = cudf.read_csv(file_path)

# Step 2: Convert the transaction_date column to datetime format
df['transaction_date'] = cudf.to_datetime(df['transaction_date'])

# Step 3: Create a new column 'month' that extracts the month from the transaction_date
df['month'] = df['transaction_date'].dt.month

# Step 4: Handle missing values in the 'amount' column
# Fill missing values in the 'amount' column with the median
median_amount = df['amount'].median()
df['amount'] = df['amount'].fillna(median_amount)

# Step 5: Create a new feature 'log_amount', which is the logarithm of the amount column
df['log_amount'] = df['amount'].log()

# Final cuDF DataFrame after all transformations
print(df.head())

# Step 6: Summary report
summary_report = """
### Data Cleaning and Feature Engineering with cuDF

**Steps Taken:**
1. Loaded the CSV data into cuDF DataFrame.
2. Converted the `transaction_date` column to datetime format.
3. Extracted the month from `transaction_date` and created a new column `month`.
4. Handled missing values in the `amount` column by filling them with the median value.
5. Created a new feature `log_amount`, which is the logarithm of the `amount` column.

**Code Quality and Efficiency:**
- The operations were performed using cuDF, which utilizes GPU acceleration to handle large datasets efficiently.
- Missing value imputation and logarithmic transformations were performed using cuDF's built-in functions, ensuring faster processing than traditional pandas.
"""

# Print summary report
print(summary_report)
