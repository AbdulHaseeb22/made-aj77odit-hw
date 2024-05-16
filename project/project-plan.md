# Project Plan

## Title

**Climate Change Analysis: Investigating the Impact of Surface Temperature and Land Cover Changes on Forest Carbon Stocks and Climate-Related Disasters**

## Main Questions

1. **Carbon and Temperature Correlation**: Is there a correlation between changes in forest carbon stocks and surface temperature changes over the decades globally and regionally?
2. **Disasters and Land Cover Changes**: How do changes in land cover influence the frequency and intensity of climate-related disasters across different regions?
3. **Integrated Impact Assessment**: What is the overall impact of rising surface temperatures and land cover changes on forest carbon stocks and the frequency of climate-related disasters?

## Description

This project aims to analyze the interrelationships between climate change metrics—namely annual surface temperature changes, forest carbon stocks, land cover changes, and the frequency of climate-related disasters. Utilizing datasets spanning several decades, the project seeks to identify trends and correlations that can help predict future environmental conditions and inform policy decisions.

The approach involves merging data from four distinct but interconnected datasets. By examining the relationships between surface temperature changes, forest carbon stocks, land cover changes, and disaster frequencies, the project aims to create a holistic view of climate dynamics. Advanced statistical models will be employed to identify patterns and predict future trends. This project not only contributes to our understanding of how different climate-related factors are interlinked but also supports the development of targeted climate resilience and mitigation strategies.

## Data Sources

### Datasource 1: Forest and Carbon Dataset

- **Metadata URL**: [IMF Forest Data](https://climatedata.imf.org/datasets/66dad9817da847b385d3b2323ce1be57/about)
- **Data URL**: [IMF Forest Data CSV](https://opendata.arcgis.com/datasets/66dad9817da847b385d3b2323ce1be57_0.csv)
- **Description**: This dataset contains data on forest area, land area, carbon stocks in forests, share of forest area, index of forest extent, and index of carbon stocks in forests from 1992 to 2020.

### Datasource 2: Annual Surface Temperature Change Dataset

- **Metadata URL**: [ IMF Surface Temperature Data](https://climatedata.imf.org/datasets/4063314923d74187be9596f10d034914/about)
- **Data URL**: [Surface Temperature Data CSV](https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv)
- **Description**: Estimates of changes in the mean surface temperature are presented, in Degree Celsius, for the years 1961-2021 by country and for World.

### Datasource 3: Climate-Related Disasters Frequency Dataset

- **Metadata URL**: [IMF Disaster Data](https://climatedata.imf.org/datasets/b13b69ee0dde43a99c811f592af4e821/about)
- **Data URL**: [IMF Disaster Data CSV](https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv)
- **Description**: This dataset provides annual frequency data of climate-related disasters from 1980 to 2022.

### Datasource 4: Land Cover Accounts Dataset

- **Metadata URL**: [IMF Land Cover Data](https://climatedata.imf.org/datasets/b1e6c0ea281f47b285addae0cbb28f4b/about)
- **Data URL**: [IMF Land Cover Data CSV](https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv)
- **Description**: This dataset includes annual land cover changes from 1992 to 2020, with data on different land cover types and their climate influence.

## Work Packages

This project is structured into five work packages, each containing specific tasks that need to be completed sequentially. Dependencies within a work package are specified in the corresponding tasks.

### WP1: Research Objectives and Data Identification [WP1](https://github.com/AbdulHaseeb22/made-aj77odit-hw/milestone/1)

- **Task 1.1**: Define the research questions. [Issue #1][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/1]
- **Task 1.2**: Identify and evaluate potential data sources. [Issue #2][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/2]
- **Task 1.3**: Finalize data sources and document their details. [Issue #3][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/3]

### WP2: Data Collection and Pipeline Development [WP2][https://github.com/AbdulHaseeb22/made-aj77odit-hw/milestone/2]

- **Task 2.1**: Download and store data in the chosen format (CSV, SQL, etc.). [Issue #4][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/4]
- **Task 2.2**: Develop data pipeline for data cleaning, preprocessing, and integration. [Issue #5][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/5]
- **Task 2.3**: Validate data pipeline and ensure data consistency. [Issue #6][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/6]

### WP3: Data Analysis and Visualization [WP3][https://github.com/AbdulHaseeb22/made-aj77odit-hw/milestone/3]

- **Task 3.1**: Conduct exploratory data analysis (EDA) and preliminary visualizations. [Issue #7][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/7]
- **Task 3.2**: Develop modules for data loading, preprocessing, visualization, and modeling. [Issue #8][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/8]
- **Task 3.3**: Perform correlation and regression analysis to answer the research questions. [Issue #9][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/9]
- **Task 3.4**: Draw conclusions and document findings. [Issue #10][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/10]

### WP4: Testing and Continuous Integration [WP4][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/10]

- **Task 4.1**: Develop and implement tests for each module. [Issue #11][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/11]
- **Task 4.2**: Set up continuous integration (CI) for automated testing and validation. [Issue #12][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/12]
- **Task 4.3**: Ensure data integrity and model performance through CI. [Issue #13][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/13]

### WP5: Reporting and Presentation [WP5][https://github.com/AbdulHaseeb22/made-aj77odit-hw/milestone/5]

- **Task 5.1**: Develop visual representations of the analysis results. [Issues #14][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/14]
- **Task 5.2**: Enhance the repository's presentation and documentation. [Issues #15][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/15]
- **Task 5.3**: Prepare the final presentation and report. [Issues #16][https://github.com/AbdulHaseeb22/made-aj77odit-hw/issues/16]
