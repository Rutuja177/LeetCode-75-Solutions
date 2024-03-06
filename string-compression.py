def compress(chars):
        if not chars:
            return []

        current_char = chars[0]
        count = 0
        index = 0
        n = len(chars)
        i = 0

        while i < n:
            if chars[i] == current_char:
                count += 1
                i += 1
            else:
                chars[index] = current_char
                current_char = chars[i]
                index += 1
                if count > 1:
                    new_count = str(count)
                    for ch in new_count:
                        chars[index] = ch
                        index += 1
                count = 0  

        chars[index] = current_char
        index += 1
        if count > 1:
            new_count = str(count)
            for ch in new_count:
                chars[index] = ch
                index += 1

        return chars[:index]



print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
