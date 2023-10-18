# How to copy collections
# You can have shallow or deep copy
# Python standard library provides you with a copy() function on the in-built collections. But, it returns only shallow copy
# In case of custom objects that you create or for deepcopy of any object, custom or in-built, you can use copy module


import copy

nums = [1, [2,3,4], 5]

nums_copy = nums # this just points to same the underlying object, so any change in nums, will be seen in nums_copy too
nums_shallow_copy = nums.copy()
nums_shallow_with_copy_module = copy.copy(nums)

print(nums, nums_copy, nums_shallow_copy, nums_shallow_with_copy_module)

# updated 1-level and 2nd level deep elements
nums[2] = 10
nums[1][1] = 8
nums[1][2] = 7

# we expect to see nums, nums_copy both will be updated
# nums_shallow_copy and nums_shallow_with_copy_module wll not have the first level updates, but the second-level updates will be there
# since they all point to the same sub-list
print(nums, nums_copy, nums_shallow_copy, nums_shallow_with_copy_module) 


# deep copy

nums_deep_copy = copy.deepcopy(nums)

nums[2] = 100
nums[1][1] = 80
nums[1][2] = 70


# none of the updates will be visible in nums_deep_copy
print(nums, nums_deep_copy)


# copy module can be used for custom objects that you create too. 