import timeit
import random


def generate_random_array(array_length: int = 1000) -> list[int]:
    """Generate random array"""
    return [random.randint(0, 1000) for _ in range(array_length)]


def insertion_sort(lst: list[int]) -> list[int]:
    """Insertion sort function"""
    for i in range(1, len(lst)):
        elem = lst[i]
        j = i - 1
        while j >= 0 and elem < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = elem
    return lst


def merge_sort(lst: list[int]) -> list[int]:
    """Merge sort function"""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left_list: list[int], right_list: list[int]) -> list[int]:
    """Merge function"""
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            merged.append(left_list[left_index])
            left_index += 1
        else:
            merged.append(right_list[right_index])
            right_index += 1
    while left_index < len(left_list):
        merged.append(left_list[left_index])
        left_index += 1
    while right_index < len(right_list):
        merged.append(right_list[right_index])
        right_index += 1
    return merged


def default_sort(lst: list[int]) -> list[int]:
    """Default sort function"""
    lst.sort()
    return lst


def measure_time(sort_func: callable, arr_list_to_sort: list[int]):
    """Measure execution time of a sorting function"""
    setup_code = f"from __main__ import {sort_func.__name__}, generate_random_array"
    test_code = f"{sort_func.__name__}({arr_list_to_sort})"
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=2, number=2)
    return min(times)


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists into one sorted list"""
    if not lists:
        return []
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if (i + 1) < len(lists) else []
            merged_lists.append(merge(list1, list2))
        lists = merged_lists
    return lists[0]


# # Example usage of merge_k_lists
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# merged_list = merge_k_lists(lists)
# print("Merged list:", merged_list)


if __name__ == "__main__":
    array_lengths = [100, 1000, 10000]
    for length in array_lengths:
        arr_list = generate_random_array(length)
        print(f"Array length: {length}")
        print(f"Insertion sort time: {measure_time(insertion_sort, arr_list)}")
        print(f"Merge sort time: {measure_time(merge_sort, arr_list)}")
        print(f"Default sort (Timsort) time: {measure_time(default_sort, arr_list)}")
