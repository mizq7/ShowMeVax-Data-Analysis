import numpy as np
import matplotlib.pyplot as plt

# Data
labels = ['Feb 2023', 'Jul 2023', 'Jan 2024', 'Apr 2024']
gender_invalid = [0.04, 0.06, 0.08, 0.08]
race_invalid = [18.05, 17.82, 59.12, 17.67]
ethnicity_invalid = [18.38, 18.05, 18.08, 17.97]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, gender_invalid, width, label='GENDER')
rects2 = ax.bar(x, race_invalid, width, label='RACE')
rects3 = ax.bar(x + width, ethnicity_invalid, width, label='ETHNICITY')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Report Date')
ax.set_ylabel('Percentage of Invalid Values')
ax.set_title('Valueset Conformance in PATIENT Entity')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Show plot
plt.show()
