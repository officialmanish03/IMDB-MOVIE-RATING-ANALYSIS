import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("merged_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# DATA CLEANING
# -----------------------------

# Convert run_length to minutes
def convert_to_minutes(x):
    try:
        parts = x.replace("min", "").split("h")
        hours = int(parts[0].strip())
        minutes = int(parts[1].strip())
        return hours * 60 + minutes
    except:
        return None

df['duration'] = df['run_length'].apply(convert_to_minutes)

# Drop missing values
df = df.dropna(subset=['rating', 'num_raters', 'duration'])

# -----------------------------
# 1. Rating vs Votes
# -----------------------------
plt.figure()
plt.scatter(df['num_raters'], df['rating'])
plt.xlabel("Number of Votes")
plt.ylabel("Rating")
plt.title("Rating vs Votes")
plt.show()

# -----------------------------
# 2. Top Movies (based on rating + votes)
# -----------------------------
top_movies = df.sort_values(by=['rating', 'num_raters'], ascending=False).head(10)
print("\nTop Movies:")
print(top_movies[['name', 'rating', 'num_raters']])

# -----------------------------
# 3. Genre Popularity
# -----------------------------
# Split genres
genres_series = df['genres'].str.split(';').explode()
top_genres = genres_series.value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 4. Duration vs Rating
# -----------------------------
plt.figure()
plt.scatter(df['duration'], df['rating'])
plt.xlabel("Duration (minutes)")
plt.ylabel("Rating")
plt.title("Duration vs Rating")
plt.show()

# -----------------------------
# 5. Year-wise Trend
# -----------------------------
yearly = df.groupby('year')['rating'].mean()

plt.figure()
yearly.plot(kind='line')
plt.title("Average Rating Over Years")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.show()

# -----------------------------
# 6. Correlation Heatmap
# -----------------------------
plt.figure()
sns.heatmap(df[['rating', 'num_raters', 'num_reviews', 'duration']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

print("\nAnalysis Completed Successfully!")