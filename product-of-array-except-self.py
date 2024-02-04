import numpy as np

def productExceptSelf(nums):
        result = []
        sample_dict = dict()

        for i in nums:
            sample_dict[i] = [num for num in nums if num != i]

        for key,value in sample_dict.items():
            product = np.prod(value)

            result.append(product)

        return result

print(productExceptSelf([1,2,3,4]))

print(productExceptSelf([-1,1,0,-3,3]))