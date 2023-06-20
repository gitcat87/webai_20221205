import pandas as pd

df = pd.read_csv(r"traintime.csv",encoding='CP949', low_memory=False)


print(df.head(5))