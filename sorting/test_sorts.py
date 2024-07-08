import random
import time

import bubble_sort
import insert_sort
import merge_sort
import quick_sort
import selection_sort


array = [30, 29, -4, 0, 0, 4, 100, 52, 42, 43, 2, 4, 4]
sorting_modules = [bubble_sort, selection_sort, insert_sort, quick_sort, merge_sort]
for module in sorting_modules:
    print(module.sort(array[:]))

big_data = list(range(10**4))
random.shuffle(big_data)
fast_sorting_modules = [quick_sort, bubble_sort, selection_sort, insert_sort, merge_sort]
for module in fast_sorting_modules:
    start = time.time()
    module.sort(big_data[:])
    print(module.__name__, time.time() - start)
