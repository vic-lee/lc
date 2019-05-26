'''
    This file contains an assortment of sorting algorithms,
    implemented in Python. The file is intended to be a
    practice while reading `Introduction to Algorithms`.

    Author: Vic Lee
'''


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
    print("unsorted: \t{}".format(unsorted_list))
    sorted_list = insertion_sort(unsorted_list)
    print("sorted: \t{}".format(sorted_list))


if __name__ == '__main__':
    main()
