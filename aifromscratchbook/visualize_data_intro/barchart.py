from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90's
histogram = Counter(min(grade // 10, 9) for grade in grades)

print(histogram)

plt.bar(
    [x + 5 for x in histogram.keys()],
    list(histogram.values()),
    10,
    edgecolor=(0, 0, 0),
)

# x-axis goes from -5.0 to 105.0, y-axis goes from 0.0 to 5.0
plt.axis((-5.0, 105.0, 0.0, 5.0))

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()
