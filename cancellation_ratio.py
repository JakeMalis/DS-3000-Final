# Compute cancellation ratio per airline and create a bar chart
agg_flights = flights_df.groupby('AIRLINE').agg(cancel_ratio=('CANCELLED', 'mean')).reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(data=agg_flights, x='AIRLINE', y='cancel_ratio')
plt.xlabel("Airline")
plt.ylabel("Cancellation Ratio")
plt.title("Cancellation Ratio by Airline")
plt.ylim(0, agg_flights['cancel_ratio'].max() * 1.1)
plt.show()