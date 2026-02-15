from __future__ import annotations

from typing import List


def heapsort(values: List[int]) -> List[int]:
    """Return a new list containing the values sorted in ascending order."""
    if len(values) < 2:
        return list(values)

    data = list(values)
    _build_max_heap(data)

    end = len(data) - 1
    while end > 0:
        data[0], data[end] = data[end], data[0]
        _sift_down(data, 0, end - 1)
        end -= 1

    return data


def _build_max_heap(data: List[int]) -> None:
    last_parent = (len(data) - 2) // 2
    for index in range(last_parent, -1, -1):
        _sift_down(data, index, len(data) - 1)


def _sift_down(data: List[int], start: int, end: int) -> None:
    root = start
    while True:
        left = 2 * root + 1
        right = left + 1
        if left > end:
            break

        swap_index = root
        if data[swap_index] < data[left]:
            swap_index = left
        if right <= end and data[swap_index] < data[right]:
            swap_index = right

        if swap_index == root:
            break

        data[root], data[swap_index] = data[swap_index], data[root]
        root = swap_index


if __name__ == "__main__":
    sample = [12, 4, 7, 1, 9, 3, 10]
    print("Input:", sample)
    print("Sorted:", heapsort(sample))
