import plotly.graph_objects as go

# Data for the sunburst chart
data = [
    ["INVENTORY", "VACCINATION_CODE_ID", "Feb 2023", 0.0],
    ["INVENTORY", "VACCINATION_CODE_ID", "Jul 2023", 0.0],
    ["INVENTORY", "VACCINATION_CODE_ID", "Jan 2024", 0.0],
    ["INVENTORY", "VACCINATION_CODE_ID", "Apr 2024", 0.0],
    ["INVENTORY", "NDC_NUMBER", "Feb 2023", 0.01],
    ["INVENTORY", "NDC_NUMBER", "Jul 2023", 0.01],
    ["INVENTORY", "NDC_NUMBER", "Jan 2024", 0.01],
    ["INVENTORY", "NDC_NUMBER", "Apr 2024", 0.01],
    ["INVENTORY", "FUNDING_SOURCE_ACTIVE_STATUS", "Feb 2023", 0.0],
    ["INVENTORY", "FUNDING_SOURCE_ACTIVE_STATUS", "Jul 2023", 0.0],
    ["INVENTORY", "FUNDING_SOURCE_ACTIVE_STATUS", "Jan 2024", 0.0],
    ["INVENTORY", "FUNDING_SOURCE_ACTIVE_STATUS", "Apr 2024", 0.0],

    ["PATIENT", "GENDER", "Feb 2023", 0.04],
    ["PATIENT", "GENDER", "Jul 2023", 0.06],
    ["PATIENT", "GENDER", "Jan 2024", 0.08],
    ["PATIENT", "GENDER", "Apr 2024", 0.08],
    ["PATIENT", "RACE", "Feb 2023", 18.05],
    ["PATIENT", "RACE", "Jul 2023", 17.82],
    ["PATIENT", "RACE", "Jan 2024", 59.12],
    ["PATIENT", "RACE", "Apr 2024", 17.67],
    ["PATIENT", "ETHNICITY", "Feb 2023", 18.38],
    ["PATIENT", "ETHNICITY", "Jul 2023", 18.05],
    ["PATIENT", "ETHNICITY", "Jan 2024", 18.08],
    ["PATIENT", "ETHNICITY", "Apr 2024", 17.97],

    ["PATIENT_VACCINATION", "VACCINATION_CODE_ID", "Feb 2023", 0.0],
    ["PATIENT_VACCINATION", "VACCINATION_CODE_ID", "Jul 2023", 0.0],
    ["PATIENT_VACCINATION", "VACCINATION_CODE_ID", "Jan 2024", 0.0],
    ["PATIENT_VACCINATION", "VACCINATION_CODE_ID", "Apr 2024", 0.0],
    ["PATIENT_VACCINATION", "VFC_CODE_ID", "Feb 2023", 5.11],
    ["PATIENT_VACCINATION", "VFC_CODE_ID", "Jul 2023", 5.63],
    ["PATIENT_VACCINATION", "VFC_CODE_ID", "Jan 2024", 4.02],
    ["PATIENT_VACCINATION", "VFC_CODE_ID", "Apr 2024", 4.13],

    ["PROVIDER", "ACTIVE_STATUS", "Feb 2023", 0.0],
    ["PROVIDER", "ACTIVE_STATUS", "Jul 2023", 0.0],
    ["PROVIDER", "ACTIVE_STATUS", "Jan 2024", 0.0],
    ["PROVIDER", "ACTIVE_STATUS", "Apr 2024", 0.0],
    ["PROVIDER", "STATE", "Feb 2023", 1.39],
    ["PROVIDER", "STATE", "Jul 2023", 1.56],
    ["PROVIDER", "STATE", "Jan 2024", 1.58],
    ["PROVIDER", "STATE", "Apr 2024", 1.53],
    ["PROVIDER", "ZIP_CODE", "Feb 2023", 1.43],
    ["PROVIDER", "ZIP_CODE", "Jul 2023", 1.6],
    ["PROVIDER", "ZIP_CODE", "Jan 2024", 1.61],
    ["PROVIDER", "ZIP_CODE", "Apr 2024", 1.56]
]

# Prepare data for sunburst
labels = [f"{item[1]} ({item[2]})" for item in data]
parents = [item[0] for item in data]
values = [item[3] for item in data]

fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total",
    hoverinfo="label+percent parent+value",
))

fig.update_layout(
    title="Valueset Conformance Across Different Entities and Time Periods",
    margin=dict(t=40, l=0, r=0, b=0)
)

fig.show()