def compress(s):
    s += "!"
    result = ""
    i = 0
    j = 0
    currentCount = 0
    while j < len(s):
        if s[j] == s[i]:
            j += 1
            currentCount += 1

        else:
            if currentCount == 1:
                result += s[i]
            else:
                result += str(currentCount) + "" + s[i]
            i = j
            currentCount = 0

    return result
