import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('Earthquakes_v2.csv')

# Ensure the timestamp is in datetime format and set it as the index
df['DATETIME'] = pd.to_datetime(df['DATETIME'])
df.set_index('DATETIME', inplace=True)

# Filter data for the last two years
current_year = pd.Timestamp.now().year
start_date = pd.Timestamp(year=current_year-1, month=1, day=1)
end_date = pd.Timestamp(year=current_year, month=12, day=31)
filtered_data = df.loc[start_date:end_date]

monthly_counts = filtered_data.resample('M').size()

plt.plot(monthly_counts.index[:len(filtered_data)], filtered_data['MAGNITUDE'])
plt.title('Monthly Earthquake Magnitude')
plt.xlabel('Date')
plt.ylabel('Magnitude')
plt.show()

model = ARIMA(monthly_counts, order=(1, 1, 1))
model_fit = model.fit()

start_index = len(monthly_counts)
end_index = start_index + 12
forecast = model_fit.predict(start=start_index, end=end_index)
