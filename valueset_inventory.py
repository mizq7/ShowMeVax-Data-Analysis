import matplotlib.pyplot as plt

# Data
dates = ['Feb 2023', 'Jul 2023', 'Jan 2024', 'Apr 2024']
vaccination_code_id = [0.0, 0.0, 0.0, 0.0]
ndc_number = [0.01, 0.01, 0.01, 0.01]
funding_source_active_status = [0.0, 0.0, 0.0, 0.0]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dates, vaccination_code_id, marker='o', label='VACCINATION_CODE_ID')
plt.plot(dates, ndc_number, marker='o', label='NDC_NUMBER')
plt.plot(dates, funding_source_active_status, marker='o', label='FUNDING_SOURCE_ACTIVE_STATUS')

# Labels and Title
plt.xlabel('Report Date')
plt.ylabel('Percentage of Invalid Values')
plt.title('Temporal Trends in Valueset Conformance in INVENTORY Entity')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
