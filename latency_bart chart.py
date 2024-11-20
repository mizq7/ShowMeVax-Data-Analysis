import numpy as np
import matplotlib.pyplot as plt

# Data
labels = ['Feb 2023', 'Jul 2023']
more_than_year = [69.0, 68.0]
less_than_year = [6.0, 6.0]
less_than_month = [1.0, 1.0]
less_than_week = [24.0, 25.0]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, more_than_year, width, label='More than a year')
rects2 = ax.bar(x, less_than_year, width, label='Less than a year')
rects3 = ax.bar(x + width, less_than_month, width, label='Less than a month')
rects4 = ax.bar(x + 2*width, less_than_week, width, label='Less than a week')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Report Date')
ax.set_ylabel('Percentage of Records')
ax.set_title('Latency of Data Reporting in All Entities')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Show plot
plt.show()
