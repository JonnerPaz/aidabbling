from collections import Counter
import matplotlib.pyplot as plt


num_friends = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
num_points = len(num_friends)
smallest_num_friends = min(num_friends)
friend_counts = Counter(num_friends)
xs = range(16)
ys = [friend_counts[x] for x in xs]


# Media en español
def average(xs: list[float]) -> float:
    return sum(xs) / len(xs)


def _median_odd(xs: list[float]) -> float:
    """If len(xs) is odd, return the middle value."""
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: list[float]) -> float:
    """If len(xs) is even, return the average of the two middle values."""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 6, hi_midpoint is 3
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


# Mediana en español
def median(v: list[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: list[float], p: float) -> float:
    """Returns the pth-percentile value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


# Moda en español
def mode(v: list[float]) -> list[float]:
    """Returns a list of the most common value(s) in v"""
    counts = Counter(v)
    max_count = max(counts.values())
    return [x for x, count in counts.items() if count == max_count]
