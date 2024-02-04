def isSubsequence(s: str, t: str):
    i = 0
    j = 0
    sub = list(s)
    word = list(t)

    while i < len(s) and j < len(word):
        if sub[i] == word[j]:
            i +=1
        j +=1
    return i == len(sub)

print(isSubsequence("abc", "ahbgdc"))