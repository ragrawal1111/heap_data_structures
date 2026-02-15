from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(order=True)
class Task:
    priority: int
    task_id: str
    arrival_time: float
    deadline: Optional[float] = None
    description: str = ""


class MaxHeapPriorityQueue:
    """Priority queue backed by a max-heap."""

    def __init__(self) -> None:
        self._heap: List[Task] = []
        self._index: Dict[str, int] = {}

    def is_empty(self) -> bool:
        return not self._heap

    def insert(self, task: Task) -> None:
        if task.task_id in self._index:
            raise ValueError(f"Task {task.task_id} already exists")

        self._heap.append(task)
        self._index[task.task_id] = len(self._heap) - 1
        self._sift_up(len(self._heap) - 1)

    def extract_max(self) -> Task:
        if not self._heap:
            raise IndexError("Priority queue is empty")

        max_task = self._heap[0]
        last = self._heap.pop()
        del self._index[max_task.task_id]

        if self._heap:
            self._heap[0] = last
            self._index[last.task_id] = 0
            self._sift_down(0)

        return max_task

    def increase_key(self, task_id: str, new_priority: int) -> None:
        index = self._get_index(task_id)
        if new_priority < self._heap[index].priority:
            raise ValueError("New priority must be greater than current priority")

        self._heap[index].priority = new_priority
        self._sift_up(index)

    def decrease_key(self, task_id: str, new_priority: int) -> None:
        index = self._get_index(task_id)
        if new_priority > self._heap[index].priority:
            raise ValueError("New priority must be less than current priority")

        self._heap[index].priority = new_priority
        self._sift_down(index)

    def _get_index(self, task_id: str) -> int:
        if task_id not in self._index:
            raise KeyError(f"Task {task_id} not found")
        return self._index[task_id]

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self._heap[parent].priority >= self._heap[index].priority:
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self._heap)
        while True:
            left = 2 * index + 1
            right = left + 1
            largest = index

            if left < size and self._heap[left].priority > self._heap[largest].priority:
                largest = left
            if right < size and self._heap[right].priority > self._heap[largest].priority:
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def _swap(self, left: int, right: int) -> None:
        self._heap[left], self._heap[right] = self._heap[right], self._heap[left]
        self._index[self._heap[left].task_id] = left
        self._index[self._heap[right].task_id] = right


if __name__ == "__main__":
    pq = MaxHeapPriorityQueue()
    pq.insert(Task(priority=5, task_id="A", arrival_time=0.0))
    pq.insert(Task(priority=2, task_id="B", arrival_time=1.0))
    pq.insert(Task(priority=9, task_id="C", arrival_time=2.0))

    pq.increase_key("B", 7)
    while not pq.is_empty():
        print(pq.extract_max())
