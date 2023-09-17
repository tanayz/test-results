import pandas as pd
df = pd.read_csv('/Users/tchowdhury/Downloads/data.txt')
df['transaction_amount'] = df.transaction_amount.astype(float)
df['transaction_time'] = pd.to_datetime(df.transaction_time).dt.date
df.sort_values(by=['transaction_time'],inplace=True)
df1 = df.groupby(by='transaction_time')['transaction_amount'].sum().rolling(3).mean()
print("January 31's rolling 3 day average of total transaction amount processed per day is ${:.2f}".format(df1[-1]))
