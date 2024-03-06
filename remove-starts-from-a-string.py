def removeStars(s: str):
    stacks = []
    for i in s:
        if i == "*":
            stacks.pop()
        else:
            stacks.append(i)

    return "".join(stacks)

print(removeStars("leet**cod*e"))