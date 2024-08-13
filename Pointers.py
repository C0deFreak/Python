# Given a list of numbers, return the indexes of all numbers whose sum is equal to target
# The output should be in format [[i1, i2]] and should not contain duplicates
nums = [3, 3, 2, 4, 5, 1, 6, 2, 7]
target = 9

res = []
nums.sort()

# Left and right pointers starting at opposite sides
l, r = 0, len(nums) - 1

# Ensures it itterates through the whole array
while l < r:
    comb = nums[l] + nums[r]

    # When the array is sorted, we combine the last and first number
    # If the sum is greater then the target, we have to reduce it, 
    # so the right pointer goes to the left where there are smaller numbers
    # if the sum is less then target, we have to enlarge the number by going right with the left pointer
    if comb > target:
        r -= 1
    elif comb < target:
        l += 1
    # If the sum is equal to the target
    else:
        # We add the soulution (indexes) to the res list
        res.append(l, r)
        # Go to the next number
        l += 1
        # And to ensure there are no duplicates we move to the right until we get a different number than the last time
        # Or until l is greater the r
        while l < r and nums[l] == nums[l-1]:
          l += 1
