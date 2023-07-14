# Accepted 1st try:
# Completed in 4:18 mins
# 60ms runtime : beats 6.31%
# 16.2 mb memory : beats 74.49%

# shitty solution 
def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

# shitty solutions is the only solution it seems.
