def uniqueOccurrences(arr):
        occur_dict = {}
        for i in arr:
            if i in occur_dict:
                occur_dict[i] +=1
            else:
                occur_dict[i] = 1

        return len(set(occur_dict.values())) == len(occur_dict.values())


print(uniqueOccurrences([[1,2,2,1,1,3]]))