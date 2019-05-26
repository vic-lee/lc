'''
    This file contains an assortment of sorting algorithms,
    implemented in Python. The file is intended to be a
    practice while reading `Introduction to Algorithms`.

    Author: Vic Lee
'''


def test_sort(sort_func):
    """Decorator that tests if a sorting algorithm is correct"""
    def wrapper(*args, **kwargs):
        unsorted_list = args[0]
        print("unsorted: \t{}".format(unsorted_list))

        sorted_list = sort_func(*args, **kwargs)
        sort_list_tested = _sort_tester(*args, **kwargs)

        if sorted_list != sort_list_tested:
            print("ERROR: sorting output incorrect")
        else:
            print("sorted: \t{}".format(sorted_list))

        return sorted_list

    return wrapper


def _sort_tester(nums: [int]) -> [int]:
    """Implemented in insertion sort"""
    LIST_SIZE = len(nums)
    for cur in range(LIST_SIZE):
        key = nums[cur]
        i = cur - 1
        while i >= 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = key
    return nums


@test_sort
def insertion_sort(nums: [int]) -> [int]:
    LIST_SIZE = len(nums)
    for cur in range(LIST_SIZE):
        key = nums[cur]
        i = cur - 1
        while i >= 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = key
    return nums


def main():
    unsorted_list = [-1, 2, 100, -3, -37, 7, 6, 99]
    sorted_list = insertion_sort(unsorted_list)


if __name__ == '__main__':
    main()
