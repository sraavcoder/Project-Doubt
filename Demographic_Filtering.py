import pandas as pd
import numpy as np

df = pd.read_csv('Articles.csv')

articles = df.sort_values('total_events')

output = articles.head(20).values.tolist()
