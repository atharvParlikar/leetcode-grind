# was not able to complete in 30 mins :(

# Brute force
def nextPermutation(nums):
    nps = {}
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            np = int(''.join([str(x) for x in nums]))
            nps[np] = (i, j)
            nums[j], nums[i] = nums[i], nums[j]

    nps = dict(sorted(nps.items(),key=lambda x:x[0],reverse = True))
    print(nps.items())
    i, j = nps[nps.items()]
    nums[i], nums[j] = nums[j], nums[i]

    
nextPermutation([1,2,3])
