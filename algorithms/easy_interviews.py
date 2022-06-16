def move_nulls_to_end(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.insert(-1, 0)
    return nums

print(move_nulls_to_end([0,2,3,0,3,5,5]))



