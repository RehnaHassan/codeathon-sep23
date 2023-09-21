import random
import timeit


def test_sort_array_performance():
    arr = [random.randint(0, 100000) for _ in range(50000)]
    start_time = timeit.default_timer()
    sorted_arr = sort_array(arr)
    end_time = timeit.default_timer()
    print(f"Sorted {len(arr)} elements in {end_time - start_time:.5f} seconds")
