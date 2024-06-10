import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the export CSV file
export_data = pd.read_csv('export_data.csv')
export_data.columns = export_data.columns.str.strip()
export_data['Start'] = pd.to_datetime(export_data['Start'], utc=True)
export_data.set_index('Start', inplace=True)
export_data.index = pd.to_datetime(export_data.index)

# Read the consumption CSV file
consumption_data = pd.read_csv('consumption_data.csv')
consumption_data.columns = consumption_data.columns.str.strip()
consumption_data['Start'] = pd.to_datetime(consumption_data['Start'], utc=True)
consumption_data.set_index('Start', inplace=True)
consumption_data.index = pd.to_datetime(consumption_data.index)

# Resample the data to a daily frequency and sum the values
daily_export = export_data.resample('D')['Export (kWh)'].sum()
daily_consumption = consumption_data.resample('D')['Consumption (kWh)'].sum()

# Calculate the net energy balance
net_energy_balance = daily_export - daily_consumption

# Resample the data to a monthly frequency and sum the values
monthly_export = export_data.resample('M')['Export (kWh)'].sum()
monthly_consumption = consumption_data.resample('M')['Consumption (kWh)'].sum()
monthly_net_balance = monthly_export - monthly_consumption

# Calculate the total annual export, consumption, and net balance
annual_export = monthly_export.sum()
annual_consumption = monthly_consumption.sum()
annual_net_balance = annual_export - annual_consumption

# Calculate the ratio of export to consumption for each month
export_consumption_ratio = monthly_export / monthly_consumption

# Create subplots for different charts
fig, axs = plt.subplots(3, 2, figsize=(16, 18))

# Plot the daily export and consumption data
axs[0, 0].plot(daily_export, marker='o', linestyle='-', color='blue', label='Export')
axs[0, 0].plot(daily_consumption, marker='o', linestyle='-', color='red', label='Consumption')
axs[0, 0].set_xlabel('Date')
axs[0, 0].set_ylabel('Energy (kWh)')
axs[0, 0].set_title('Daily Solar Energy Export and Consumption')
axs[0, 0].legend()
axs[0, 0].grid(True)
axs[0, 0].set_xlim(daily_export.index.min(), daily_export.index.max())
axs[0, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Plot the net energy balance
axs[0, 1].plot(net_energy_balance, marker='o', linestyle='-', color='green')
axs[0, 1].set_xlabel('Date')
axs[0, 1].set_ylabel('Net Energy Balance (kWh)')
axs[0, 1].set_title('Daily Net Energy Balance')
axs[0, 1].grid(True)
axs[0, 1].set_xlim(net_energy_balance.index.min(), net_energy_balance.index.max())
axs[0, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Plot the monthly export and consumption data
axs[1, 0].plot(monthly_export, marker='o', linestyle='-', color='blue', label='Export')
axs[1, 0].plot(monthly_consumption, marker='o', linestyle='-', color='red', label='Consumption')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Energy (kWh)')
axs[1, 0].set_title('Monthly Solar Energy Export and Consumption')
axs[1, 0].legend()
axs[1, 0].grid(True)
axs[1, 0].set_xlim(monthly_export.index.min(), monthly_export.index.max())
axs[1, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Plot the monthly net energy balance
axs[1, 1].plot(monthly_net_balance, marker='o', linestyle='-', color='green')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Net Energy Balance (kWh)')
axs[1, 1].set_title('Monthly Net Energy Balance')
axs[1, 1].grid(True)
axs[1, 1].set_xlim(monthly_net_balance.index.min(), monthly_net_balance.index.max())
axs[1, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Display the highest and lowest net energy balance months
highest_month = monthly_net_balance.idxmax().strftime('%B')
lowest_month = monthly_net_balance.idxmin().strftime('%B')
axs[2, 0].text(0.5, 0.5, f"Highest Net Balance Month: {highest_month}\nLowest Net Balance Month: {lowest_month}",
               fontsize=14, ha='center', va='center')
axs[2, 0].axis('off')

# Display the total annual export, consumption, and net balance
axs[2, 1].text(0.5, 0.5, f"Annual Export: {annual_export:.2f} kWh\nAnnual Consumption: {annual_consumption:.2f} kWh\nAnnual Net Balance: {annual_net_balance:.2f} kWh",
               fontsize=14, ha='center', va='center')
axs[2, 1].axis('off')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()

# Print the export to consumption ratio for each month
print("Export to Consumption Ratio:")
for month, ratio in export_consumption_ratio.items():
    print(f"{month.strftime('%B')}: {ratio:.2f}")