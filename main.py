import numpy as np
import pandas as pd

#  -- FILE 1 --

# Load file
df = pd.read_csv('files/1 - fee flash data.csv')

# Filter rows that contain 'PGB'
df = df.loc[df['Posting type'] == 'Sales order revenue']

# Remove Columns
columnsToKeep = ['Date', 'Voucher', 'Ledger account',
                 'Amount in transaction currency']
df.drop(df.columns.difference(columnsToKeep), 1, inplace=True)


# Filter rows that contain 'PGB'
df = df.loc[df['Ledger account'].str.contains('PGB')]
df['Ledger account'] = df['Ledger account'].str.extract(
    '(PGB.*-)', expand=False)
df['Ledger account'] = df['Ledger account'].str.split('-').str[0]

# Reverse sign of 'Amount in transaction currency'
df['Amount in transaction currency'] = df['Amount in transaction currency'].str.replace(
    ',', '')
df['Amount in transaction currency'] = pd.to_numeric(
    df['Amount in transaction currency'])
df['Amount in transaction currency'] = df['Amount in transaction currency'] * -1

df.to_excel(
    f'result_2.xlsx', index=False)


#  -- FILE 2 --

# Add new columns
df['Category'] = 'INTERCO'
df['Sales currency'] = 'GBP'
df['Revenue'] = df['Amount in transaction currency']
df['Activity number'] = ''

# Rename Columns
df.rename(columns={
    'Date': 'Project date',
    'Ledger account': 'Project ID',
    'Amount in transaction currency': 'Sales amount',
    'Voucher': 'Description'
}, inplace=True)

# Re-order Columns
df = df[['Project date', 'Project ID', 'Category', 'Sales amount', 'Sales currency', 'Revenue',
         'Activity number', 'Description']]


df.to_excel(
    f'result_3.xlsx', index=False)


print(df)
