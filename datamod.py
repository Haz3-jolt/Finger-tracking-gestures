import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse

# Read the log file
with open('pain_log.txt', 'r') as f:
    lines = f.readlines()

# Extract the timestamps and convert to pandas datetime objects
timestamps = [parse(line.split('at ')[1].strip()) for line in lines]
series = pd.Series(1, index=timestamps)

# Resample to get the count per hour
resampled = series.resample('H').sum()

# Create a new index that includes all hours of the day
start = resampled.index.min().replace(hour=0, minute=0, second=0)
end = resampled.index.max().replace(hour=23, minute=59, second=59)
new_index = pd.date_range(start, end, freq='H')

# Reindex the resampled series
resampled = resampled.reindex(new_index, fill_value=0)

# Plot the data
plt.figure(figsize=(10,6))
resampled.plot(kind='bar')
plt.xlabel('Time')
plt.ylabel('Number of pain reports')
plt.title('Pain reports per hour')
plt.show()