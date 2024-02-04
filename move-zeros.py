def moveZeroes(nums):
    zero_list = [i for i in nums if i == 0]
    non_zero = [i for i in nums if i != 0]
    nums[:] = non_zero + zero_list
    print(nums)

moveZeroes([0,1,0,3,12])

#2-pointer apprpach:

def moveZeroes(nums):
        j = 0 
        for i in range(len(nums)):
           if nums[i] != 0:
               nums[j], nums[i] = nums[i], nums[j]
               j += 1
        print(nums)