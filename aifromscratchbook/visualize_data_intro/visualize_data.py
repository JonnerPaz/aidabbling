from matplotlib import pyplot as plt

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
# # Create a line chart, years on the x-axis, GDP on the y-axis
# plt.plot(years, gdp, color="green", marker="o", linestyle="solid")
#
# plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")
# plt.show()

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Create a bar chart, movies on the x-axis, number of Oscars on the y-axis
plt.bar(range(len(movies)), num_oscars)

plt.ylabel("Number of Oscars")
plt.xticks(range(len(movies)), movies)

plt.axis((0, 5, 0, 15))

plt.show()
