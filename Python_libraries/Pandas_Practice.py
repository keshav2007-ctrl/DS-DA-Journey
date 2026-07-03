import pandas as pd

# print(df.head())
# print(df.shape)
# print(df.describe())

# # How many unique nationalities?
# print(df['nationality'].nunique())

# # Which nationality has the most players?
# print(df['nationality'].value_counts().head(10))

# # Average age of all players
# print(df['age'].mean())

# # Filter only Spanish players
# spanish = df[df['nationality'] == 'Spanish']
# print(spanish.shape)

# # Top 5 players by tournament rating
# print(df.sort_values('tournament_rating', ascending=False).head())

# # Average tournament rating by nationality (top 10)
# print(df.groupby('nationality')['tournament_rating'].mean().sort_values(ascending=False).head(10))

# # Youngest and oldest player
# print(df['age'].min(), df['age'].max())

# # Players above average rating
# avg = df['tournament_rating'].mean()
# top = df[df['tournament_rating'] > avg]
# print(top.shape)

# s = pd.Series([1, 2, 3, 4, 5])
# print(s)

# df = pd.read_csv('archive/fifa_world_cup_2026_player_performance.csv')
# df["player_name"][0] = "Lionel Messi", Pandas does not allow direct assignment to a single cell in a DataFrame using the bracket notation.
# print(df)

Dict1 = {"Name": ["Alice", "Bob", "Charlie", "David"],
         "Age": [25, 30, 35, 40],
         "City": ["New York", "Los Angeles", "Chicago", "Houston"]}

df = pd.DataFrame(Dict1)

df.index = ["1", "2", "3", "4"]
df.to_csv("dict1.csv", index=True)
print(pd.read_csv("dict1.csv", index_col=0))