#O(n^2)

def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            

#using hashmap: O(n)

def twoSum(self, nums, target):
    hashmap = {}

    for i in range(len(nums)):
        if nums[i] in hashmap:
            return [i, hashmap[nums[i]]]
        else:
            hashmap[target - nums[i]] = i
            