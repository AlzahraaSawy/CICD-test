import pandas as pd

data = {

    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
df['Age'] = df['Age'] + 1
df.to_csv('output.csv', index=False)

print("ETL process completed successfully.") 