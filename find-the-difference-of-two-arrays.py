def findDifference(nums1, nums2):
    list1 = []
    list2 = []
    for i in nums1:
        if i not in nums2 and i not in list1:
            list1.append(i)

    for i in nums2:
        if i not in nums1 and i not in list2:
            list2.append(i)
    
    return [list1, list2]

print(findDifference([1,2,3],[2,4,6]))