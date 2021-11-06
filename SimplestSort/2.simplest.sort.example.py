def simplest_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            print(nums)
        print()

print("Case 1: Alread Sorted")
nums = [1, 2, 3, 4, 5]
simplest_sort(nums)

print("Case 2: Reversed")
nums = [5, 4, 3, 2, 1]
simplest_sort(nums)

print("Case 3: Average Case")
nums = [3, 2, 5, 1, 4]
simplest_sort(nums)


