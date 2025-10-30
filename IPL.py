import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print(matches.head())
print(deliveries.head())

matches.info()
matches.isnull().sum()

team_wins = matches['winner'].value_counts().head(10)
print(team_wins)

pom = matches['player_of_match'].value_counts().head(10)
print(pom)

sns.countplot(x='toss_decision', data=matches)
plt.title("Toss")
plt.show()

team_wins.plot(kind='bar', color='skyblue')
plt.title("Win percentage by team")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.show()

matches_per_year = matches['season'].value_counts().sort_index()
matches_per_year.plot(kind='bar', color='skyblue')
plt.title("Matches played per year")
plt.xlabel("Year")
plt.ylabel("Matches")
plt.show()

top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
top_batsmen.plot(kind='bar', color='skyblue')
plt.title('Top batsmen')
plt.xlabel('Batsman')
plt.ylabel('Runs')
plt.show()