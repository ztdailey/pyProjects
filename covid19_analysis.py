import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from covid19_datapull import data

# Read csv with IO
data = io.StringIO(data.decode('utf-8'))

# Reading covid19 data and turning it into a pandas data frame
df = pd.read_csv(data)

# Remove columns likely to be unused, todo consider reviewing again later
df.drop('stringency_index', axis=1, inplace=True)

pd.to_datetime(df.date)

#print(df.describe())
#print(df.location.value_counts())

latest = df.loc[:, ['iso_code', 'continent', 'location', 'date', 'population', 'people_fully_vaccinated'] ]
latest = latest.sort_values('date').groupby('location').tail(1)

# Calculate percentage of total population vaccinated
latest['pop_vaccd'] = latest['people_fully_vaccinated'] / latest['population']
latest = latest.sort_values(['pop_vaccd'], ascending=False)

latest.to_csv(r'C:\Users\zachd\Documents\Code\pyProjects\latest_vacc_rate.csv', index=False)