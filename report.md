# Assignment 4: Heap Data Structures

## Heapsort Implementation

The Heapsort algorithm is implemented using a max-heap backed by a Python list. The heap is built in-place in $O(n)$ time using bottom-up heap construction. The maximum element (root) is repeatedly swapped to the end of the list, the heap size is reduced by one, and the heap property is restored with a sift-down operation.

Key steps:
- Build a max-heap in-place.
- Repeatedly extract the maximum by swapping the root with the last element.
- Restore heap order with `sift_down` after each extraction.

## Time Complexity Analysis

### Worst Case
Building the heap is $O(n)$. Each of the $n$ extractions costs $O(\log n)$, so the total is $O(n \log n)$.

### Average Case
The extraction phase still dominates, and each `sift_down` is $O(\log n)$ on average. The total time remains $O(n \log n)$.

### Best Case
Even if the input is already sorted, heap construction and extraction still perform the same asymptotic amount of work. The total remains $O(n \log n)$.

### Why Heapsort is $O(n \log n)$ in All Cases
Heapsort always performs $n$ extractions, and each extraction performs a bounded number of swaps and comparisons proportional to $\log n$. The heap height is $\lfloor \log_2 n \rfloor$, so each `sift_down` is $O(\log n)$ regardless of input order. Therefore, the total time is $O(n \log n)$ for all cases.

## Space Complexity
Heapsort is in-place for the array representation, using $O(1)$ auxiliary space beyond the input array. The only overhead is a small, constant number of extra variables.

## Empirical Comparison
The benchmarking script compares Heapsort, Quicksort, and Mergesort across sorted, reverse-sorted, and random inputs.

To run:
```
python benchmark.py
```

### Results (fill after running)

| Input Size | Distribution | Heapsort (s) | Quicksort (s) | Mergesort (s) |
|-----------:|--------------|--------------|---------------|---------------|
| 1000       | sorted       | 0.002353     | 0.000667      | 0.001245      |
| 1000       | reverse      | 0.002033     | 0.001254      | 0.001272      |
| 1000       | random       | 0.002209     | 0.000880      | 0.001869      |
| 5000       | sorted       | 0.014551     | 0.004159      | 0.006917      |
| 5000       | reverse      | 0.013462     | 0.007203      | 0.007218      |
| 5000       | random       | 0.014042     | 0.005434      | 0.010738      |
| 10000      | sorted       | 0.031896     | 0.008997      | 0.014893      |
| 10000      | reverse      | 0.029814     | 0.017138      | 0.015249      |
| 10000      | random       | 0.032170     | 0.011263      | 0.024776      |
| 20000      | sorted       | 0.073761     | 0.019586      | 0.032395      |
| 20000      | reverse      | 0.068413     | 0.034497      | 0.033628      |
| 20000      | random       | 0.071414     | 0.025215      | 0.051175      |

### Discussion

Observed results should align with theory:
- Heapsort tends to be slower than Quicksort on random data due to higher constant factors.
- Quicksort is fastest across these trials; using a median-of-three pivot avoids worst-case behavior on sorted inputs.
- Mergesort provides stable $O(n \log n)$ performance but uses additional memory.

## Priority Queue Implementation

The priority queue uses a max-heap represented by a Python list to support $O(\log n)$ insertion and extraction. A dictionary maps `task_id` to heap index to enable efficient `increase_key` and `decrease_key` operations.

### Data Structure Choice
A list provides contiguous storage, cache-friendly access, and simple index arithmetic for parent/child relationships. It also supports $O(1)$ append for insertions.

### Task Model
Each task stores:
- `task_id` (unique identifier)
- `priority`
- `arrival_time`
- `deadline` (optional)
- `description` (optional)

### Operation Complexity
- `insert`: $O(\log n)$ due to `sift_up`.
- `extract_max`: $O(\log n)$ due to `sift_down`.
- `increase_key`: $O(\log n)$ due to `sift_up`.
- `decrease_key`: $O(\log n)$ due to `sift_down`.
- `is_empty`: $O(1)$.

## Scheduling Simulation Notes

The scheduler uses a max-heap, so the task with the highest priority is extracted first. The provided implementation includes a simple demo in `priority_queue.py` and can be extended with a full simulation if desired.

## Key Takeaways

- Understand array-based heap indexing and parent/child relationships.
- Be able to explain `sift_up` and `sift_down` and why they are $O(\log n)$.
- Know why Heapsort is $O(n \log n)$ regardless of input order.
- Compare Heapsort, Quicksort, and Mergesort empirically and theoretically.
- Connect heap-based priority queues to scheduling and task management.
