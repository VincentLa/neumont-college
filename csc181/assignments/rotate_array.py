def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_copy = nums.copy()
    
    for i in range(len(nums)):
        nums[i] = nums_copy[(i - k) % len(nums)]
    
    return nums 

nums = [1, 2]
k = 3
print(rotate(nums, k))