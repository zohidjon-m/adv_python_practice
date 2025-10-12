# Assignment 5: Bubble Sort implementation
def bubble_sort(numbers):
    n = len(numbers)
    nums = numbers[:]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

raw = input("Enter numbers separated by spaces: ").strip()
arr = [int(x) for x in raw.split()]
sorted_arr = bubble_sort(arr)
print("Sorted:", sorted_arr)