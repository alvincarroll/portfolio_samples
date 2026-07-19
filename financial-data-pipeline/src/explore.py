import polars as pl

raw_data = pl.read_csv(r'financial-data-pipeline\data\raw\Coffee_sales.csv')

print(raw_data.describe())




