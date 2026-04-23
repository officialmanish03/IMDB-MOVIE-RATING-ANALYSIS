# IMDB-MOVIE-RATING-ANALYSIS
Exploratory Data Analysis (EDA) on a 1,500-entry IMDB dataset using Python, Pandas, Matplotlib, and Seaborn.

This project performs in-depth analysis on an IMDB movie dataset to uncover patterns in ratings, genres, popularity, and release trends. It covers the full EDA pipeline — from data cleaning to visualization.
📊 Analyses Performed

Rating vs Votes — Scatter plot exploring the popularity-quality relationship
Top Movies — Ranked by combined rating & vote count
Genre Popularity — Bar chart of the top 10 most frequent genres
Duration vs Rating — Does runtime affect audience score?
Year-wise Trend — Average rating evolution across decades
Correlation Heatmap — Inter-variable relationships using Seaborn

🛠️ Tech Stack
Python Pandas Matplotlib Seaborn
📁 Dataset
CSV file with 1,500 IMDB movie entries containing fields: name, rating, num_raters, num_reviews, genres, run_length, year
▶️ How to Run
bashpip install pandas matplotlib seaborn
python imdb_analysis.py
