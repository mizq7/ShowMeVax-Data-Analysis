import matplotlib.pyplot as plt
import numpy as np

# Data
dates = ['Feb 2023', 'Jul 2023', 'Jan 2024', 'Apr 2024']

# INVENTORY entity
inventory_vaccination_code_id = [0.0, 0.0, 0.0, 0.0]
inventory_ndc_number = [0.01, 0.01, 0.01, 0.01]
inventory_funding_source_active_status = [0.0, 0.0, 0.0, 0.0]

# PATIENT entity
patient_gender = [0.04, 0.06, 0.08, 0.08]
patient_race = [18.05, 17.82, 59.12, 17.67]
patient_ethnicity = [18.38, 18.05, 18.08, 17.97]

# PATIENT_VACCINATION entity
patient_vaccination_code_id = [0.0, 0.0, 0.0, 0.0]
patient_vfc_code_id = [5.11, 5.63, 4.02, 4.13]

# PROVIDER entity
provider_active_status = [0.0, 0.0, 0.0, 0.0]
provider_state = [1.39, 1.56, 1.58, 1.53]
provider_zip_code = [1.43, 1.6, 1.61, 1.56]

x = np.arange(len(dates))

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the data
ax.plot(x, inventory_vaccination_code_id, marker='o', label='INVENTORY: VACCINATION_CODE_ID')
ax.plot(x, inventory_ndc_number, marker='o', label='INVENTORY: NDC_NUMBER')
ax.plot(x, inventory_funding_source_active_status, marker='o', label='INVENTORY: FUNDING_SOURCE_ACTIVE_STATUS')

ax.plot(x, patient_gender, marker='s', label='PATIENT: GENDER')
ax.plot(x, patient_race, marker='s', label='PATIENT: RACE')
ax.plot(x, patient_ethnicity, marker='s', label='PATIENT: ETHNICITY')

ax.plot(x, patient_vaccination_code_id, marker='^', label='PATIENT_VACCINATION: VACCINATION_CODE_ID')
ax.plot(x, patient_vfc_code_id, marker='^', label='PATIENT_VACCINATION: VFC_CODE_ID')

ax.plot(x, provider_active_status, marker='d', label='PROVIDER: ACTIVE_STATUS')
ax.plot(x, provider_state, marker='d', label='PROVIDER: STATE')
ax.plot(x, provider_zip_code, marker='d', label='PROVIDER: ZIP_CODE')

# Adding labels and title
ax.set_xlabel('Report Date')
ax.set_ylabel('Percentage of Invalid Values')
ax.set_title('Temporal Trends in Valueset Conformance')
ax.set_xticks(x)
ax.set_xticklabels(dates)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(True)

# Display the plot
plt.tight_layout()
plt.show()