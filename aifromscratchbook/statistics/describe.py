from collections import Counter
import math
from linear_algebra.vectors import sum_of_squares
from linear_algebra.vectors import dot
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


def data_range(v: list[float]) -> float:
    return max(v) - min(v)


def de_average(xs: list[float]) -> list[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = average(xs)
    return [x - x_bar for x in xs]


def variance(xs: list[float]) -> float:
    """Almost the average squared distance from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_average(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: list[float]) -> float:
    return math.sqrt(variance(xs))


def interquartile_range(v: list[float]) -> float:
    return quantile(v, 0.75) - quantile(v, 0.25)


def covariance(xs: list[float], ys: list[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must be the same length"
    return dot(de_average(xs), de_average(ys)) / (len(xs) - 1)


def correlation(xs: list[float], ys: list[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0
