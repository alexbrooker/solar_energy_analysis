# Solar Energy Analysis for Smart Meter Export Data

Welcome to the Solar Energy Analysis project! This repository contains code and data for analyzing solar energy export and consumption data from a residential solar system, exported from the UK octopus website. The goal of this project is to provide insights into the performance of the solar system, identify trends and patterns, and assess the overall energy balance.

![Figure_1](https://github.com/alexbrooker/solar_energy_analysis/assets/23118281/1c08c149-7b51-4e33-a2c2-75f9f6770270)

## Table of Contents
- [Introduction](#introduction)
- [Data](#data)
- [Analysis](#analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Solar Energy Analysis project aims to help homeowners and researchers understand the performance of residential solar systems by analyzing exported and consumed energy data. By visualizing and exploring the data, we can gain valuable insights into the system's efficiency, seasonal variations, and the extent to which solar energy covers the household's energy needs.

## Data
The repository includes two CSV files containing the solar energy export and consumption data:
- `export_data.csv`: Contains the exported energy data from the solar system, with columns for timestamp and exported energy in kWh.
- `consumption_data.csv`: Contains the consumed energy data from the household, with columns for timestamp and consumed energy in kWh.

The data covers a period from 2nd June 2023 to 10th Jue 2024 and is recorded at 30-minute intervals.

Example data:
| Export (kWh) | Start | End |
| --- | --- | --- |
| 0.03400000000000000000 | 2023-06-02T01:00:00+01:00 | 2023-06-02T01:30:00+01:00 |
| 0.03500000000000000000 | 2023-06-02T01:30:00+01:00 | 2023-06-02T02:00:00+01:00 |
| 0.03400000000000000000 | 2023-06-02T02:00:00+01:00 | 2023-06-02T02:30:00+01:00 |
| 0.03500000000000000000 | 2023-06-02T02:30:00+01:00 | 2023-06-02T03:00:00+01:00 |
| 0.03400000000000000000 | 2023-06-02T03:00:00+01:00 | 2023-06-02T03:30:00+01:00 |
| 0.03500000000000000000 | 2023-06-02T03:30:00+01:00 | 2023-06-02T04:00:00+01:00 |

## Analysis
The analysis is performed using Python and various data analysis and visualization libraries, including:
- pandas: For data manipulation and analysis
- matplotlib: For creating visualizations
- numpy: For numerical computations

The main analysis steps include:
1. Data preprocessing and cleaning
2. Resampling the data to daily and monthly frequencies
3. Calculating the net energy balance (export - consumption)
4. Identifying the months with the highest and lowest net energy balance
5. Calculating the total annual export, consumption, and net balance
6. Analyzing the ratio of export to consumption for each month

## Installation
To run the analysis code locally, follow these steps:
1. Clone the repository:
   ```
   git clone https://github.com/your-username/solar-energy-analysis.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To perform the solar energy analysis, run the `solar_energy_analysis.py` script:
```
python solar_energy_analysis.py
```

The script will generate visualizations and print the export to consumption ratio for each month.

## Results
The analysis provides several key findings and visualizations, including:
- Daily solar energy export and consumption trends
- Daily net energy balance
- Monthly solar energy export and consumption patterns
- Monthly net energy balance
- Identification of the months with the highest and lowest net energy balance
- Total annual export, consumption, and net balance
- Export to consumption ratio for each month

These results offer valuable insights into the performance and efficiency of the residential solar system, helping homeowners optimize their energy usage and understand the benefits of solar energy.

## Contributing
Contributions to the Solar Energy Analysis project are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the existing code style and provide clear descriptions of your changes.

## License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize and expand upon this README file based on your specific project details, add more sections if needed, and include any additional information that would be helpful for users and contributors.
