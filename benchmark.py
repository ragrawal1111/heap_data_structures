from __future__ import annotations

import random
import time
from typing import Callable, List

from heapsort import heapsort


def quicksort(values: List[int]) -> List[int]:
    data = list(values)
    _quicksort(data, 0, len(data) - 1)
    return data


def _quicksort(data: List[int], low: int, high: int) -> None:
    while low < high:
        pivot_index = _partition(data, low, high)
        left_size = pivot_index - low
        right_size = high - pivot_index

        if left_size < right_size:
            _quicksort(data, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quicksort(data, pivot_index + 1, high)
            high = pivot_index - 1


def _partition(data: List[int], low: int, high: int) -> int:
    pivot_index = _median_of_three(data, low, high)
    data[pivot_index], data[high] = data[high], data[pivot_index]
    pivot = data[high]
    i = low
    for j in range(low, high):
        if data[j] <= pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return i


def _median_of_three(data: List[int], low: int, high: int) -> int:
    mid = (low + high) // 2
    a = data[low]
    b = data[mid]
    c = data[high]

    if a <= b <= c or c <= b <= a:
        return mid
    if b <= a <= c or c <= a <= b:
        return low
    return high


def mergesort(values: List[int]) -> List[int]:
    if len(values) < 2:
        return list(values)

    mid = len(values) // 2
    left = mergesort(values[:mid])
    right = mergesort(values[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged: List[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def generate_data(size: int, distribution: str) -> List[int]:
    if distribution == "sorted":
        return list(range(size))
    if distribution == "reverse":
        return list(range(size, 0, -1))
    if distribution == "random":
        data = list(range(size))
        random.shuffle(data)
        return data
    raise ValueError(f"Unknown distribution: {distribution}")


def time_algorithm(name: str, func: Callable[[List[int]], List[int]], data: List[int]) -> float:
    start = time.perf_counter()
    result = func(data)
    end = time.perf_counter()

    if result != sorted(data):
        raise AssertionError(f"{name} failed to sort correctly")

    return end - start


def run_benchmarks() -> None:
    algorithms = {
        "Heapsort": heapsort,
        "Quicksort": quicksort,
        "Mergesort": mergesort,
    }
    sizes = [1000, 5000, 10000, 20000]
    distributions = ["sorted", "reverse", "random"]

    print("Benchmark results (seconds):")
    for size in sizes:
        for distribution in distributions:
            data = generate_data(size, distribution)
            print(f"\nSize={size}, Distribution={distribution}")
            for name, func in algorithms.items():
                duration = time_algorithm(name, func, data)
                print(f"  {name:10s}: {duration:.6f}")


if __name__ == "__main__":
    run_benchmarks()
