# Restaurant-Tips-Analysis-project
Data Analyst project performing EDA on a restaurant dataset. Includes full data pipeline: cleaning (duplicate removal &amp; median/mode imputation), statistical aggregation, and visualization (Seaborn). Key insights into revenue trends, tipping behavior, and correlation metrics. Future-proof code following modern Pandas standards.

1. Data Wrangling & Cleaning
I didn't just load data; I actively managed its quality.

Duplicate Handling: I used df.drop_duplicates() to ensure data integrity.

Missing Value Imputation: I applied statistical logic by filling categorical missing values with the mode and numerical ones with the median.

Modern Pandas Standards: My code follows current best practices by avoiding the deprecated inplace=True and using assignment instead.

2. Statistical Analysis (EDA :- Exploratory Data Analysis)
I moved beyond just looking at the data to extracting business insights.

Aggregation: I used groupby and agg to calculate both the "typical" (mean) and "total" (sum) performance metrics for tips and bills across different days.

Correlation: I calculated a correlation matrix (df.corr) to understand how different variables relate to each other mathematically.

3. Data Visualization & Reporting
I demonstrated that i can communicate my findings visually.

Chart Variety: I used Bar plots for revenue, Scatter plots for relationships, Box plots for outliers, and Heatmaps for multi-variable correlation.

Professionalism: I used sns.set_theme and added proper labels and titles to make my charts readable for others.

Exporting Results: I successfully automated the process of saving these insights to files (e.g., daily_revenue.png) and logging output to analysis_output.txt.
