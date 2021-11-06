def simplest_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

import random
pops = [i for i in range(10, 100)]
nums = random.sample(pops, 10)
simplest_sort(nums)
if nums == sorted(nums):
    print("SORTED!")
else:
    print("OOPS!!!")
