import matplotlib.pyplot as plt

# Data
dates = ['Feb 2023', 'Jul 2023', 'Jan 2024', 'Apr 2024']
gender_invalid = [0.04, 0.06, 0.08, 0.08]
race_invalid = [18.05, 17.82, 59.12, 17.67]
ethnicity_invalid = [18.38, 18.05, 18.08, 17.97]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dates, gender_invalid, marker='o', label='GENDER')
plt.plot(dates, race_invalid, marker='o', label='RACE')
plt.plot(dates, ethnicity_invalid, marker='o', label='ETHNICITY')

# Labels and Title
plt.xlabel('Report Date')
plt.ylabel('Percentage of Invalid Values')
plt.title('Temporal Trends in Valueset Conformance in PATIENT Entity')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
