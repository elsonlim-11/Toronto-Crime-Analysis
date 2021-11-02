# Toronto Crime Analysis
## Description
 An end-to-end data project transforming raw Toronto Police data into an interactive data app

## License and Disclaimer
This project is intended to be a demonstration of working with different data types, analytical tools and cloud technologies. This is not meant to provide live or accurate crime data in any official capcity. Use of this data follows the Open Government License of Ontario.

## Questions
* What neighbourhood should I avoid? 
* How has crime been trending?
* What are the predictors of high crime neighbourhoods?
* Which neighbourhoods are most similar to the ones I like?


## Constraints
1. Use Azure Blob Storage for Data Lake and Synapse for Data Warehouse capabilities
2. Data should be queried, ingested, transformed and loaded entirely on a Python environment (no GUI)
3. Project should demonstrate data engineering (Azure, Airflow, CI/CD), data analysis (Plotly, Stremlit, Power BI) and data science (ARIMA, Clustering, A/B, Geo Polygons, Haversine distance)


## Project Plan
** Data engineering **
1. Download Toronto police data from: https://data.torontopolice.on.ca/pages/catalogue
2. Create blob storage for raw csvs, lake storage for processed parquets and Synapse workspace for queries
3. Upload files from local folder/Git repository to Azure Blob Storage
4. Enforce schema and perform transformations on data using an on-demand Databricks cluster (split into fact and dim)
5. Sink output to Azure Gen2 Lake Storage as partitioned parquets
6. Apply idempotency to insert parquet files into data warehouse
7. Create Airflow to run steps 3-6 regularly

** Data analysis **
1. Link PowerBI to Synapse 
2. Query Synapse using Python; visualize with plotLy and Streamlit

** Data science **
1. ARIMA on forecasted crime rates by crime and neighbourhood
2. Clustering for similar neighbourhoods by crime (and census) stats
3. A/B testing for proximity of merchant/point of interest type X to crime type Y (apply Haversine and polygons)



