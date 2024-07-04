# Exercise Badges

![](https://byob.yarr.is/AbdulHaseeb22/made-aj77odit-hw/score_ex1) ![](https://byob.yarr.is/AbdulHaseeb22/made-aj77odit-hw/score_ex2) ![](https://byob.yarr.is/AbdulHaseeb22/made-aj77odit-hw/score_ex3) ![](https://byob.yarr.is/AbdulHaseeb22/made-aj77odit-hw/score_ex4) ![](https://byob.yarr.is/AbdulHaseeb22/made-aj77odit-hw/score_ex5)
# Correlation Between Changes in Forest Carbon Stocks and Surface Temperature Changes

## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Data Pipeline](#data-pipeline)
- [Analysis Summary](#analysis-summary)
- [Conclusion](#conclusion)
- [Repository Structure](#repository-structure)
- [License](#license)
- [Getting Started](#getting-started)
- [Version Control Steps](#version-control-steps)

## Project Overview
This project investigates the correlation between changes in forest carbon stocks and surface temperature changes globally. Forests play a crucial role in sequestering carbon dioxide, which helps mitigate climate change. The primary question addressed is: **"How do changes in forest carbon stocks correlate with surface temperature changes?"**

Understanding this correlation provides insights into the effectiveness of forests in combating climate change and informs environmental policies and conservation efforts.

## Data Sources
The project utilizes the following datasets:

- **Annual Surface Temperature Change**: Mean surface temperature changes relative to a baseline climatology period of 1951-1980 for each country.
- **Forest and Carbon Stocks**: Information about carbon stocks in forests for various countries over several years.

## Data Pipeline
The data pipeline consists of three main modules:

1. **Extractor**: Extracts data from specified URLs.
2. **Transform**: Filters and transforms the data, including calculating year-over-year differences.
3. **Loader**: Loads the transformed data into an SQLite database.

The ETL process ensures data quality, consistency, and alignment with the research questions.

![ETL Pipeline Diagram](path/to/etl_pipeline_diagram.png)

## Analysis Summary
The analysis was performed to investigate the correlation between changes in forest carbon stocks and surface temperature changes:

1. **Data Loading and Merging**:
   - Loaded processed data from the SQLite database.
   - Merged temperature and carbon stock datasets based on the 'Country' column.

2. **Correlation Calculation**:
   - Calculated global year-over-year changes in temperature and carbon stocks.
   - Computed correlation coefficients between temperature and carbon stock changes for each year.
   - Identified average correlations for each country to highlight significant patterns.

### Key Findings
- The year-over-year changes in global temperature and carbon stocks exhibit distinct patterns, with temperature changes showing minor annual variations and carbon stocks showing more significant fluctuations.
- The correlation between temperature and carbon stock changes is inconsistent over the years, indicating a complex relationship influenced by multiple factors.
- Discrepancies in country names between the datasets and the shapefile hindered the visualization of country-specific correlations on a world map.

## Conclusion
The analysis indicates that there is no consistent, strong correlation between changes in forest carbon stocks and surface temperature changes globally. The correlation coefficients vary significantly across different years, suggesting that other factors may influence these variables.

### Limitations
- The analysis faced challenges due to unmatched country names, affecting the visualization of country-specific correlations.
- The study only considers year-over-year changes and does not account for long-term trends or other influencing factors.

### Future Work
To improve the analysis, it is essential to ensure consistency in country names across all datasets. Additionally, incorporating long-term trends and other environmental factors could provide a more comprehensive understanding of the relationship between forest carbon stocks and surface temperature changes.

## Repository Structure
