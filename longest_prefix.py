def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    min_length = len((min(strs, key=len)))
    retvalue = ''
    for i in range(min_length):
        for j in range(len(strs) - 1):
            if strs[j][i] == strs[j+1][i] and j == (len(strs) - 2) and i == len(retvalue):
                retvalue += strs[j][i]
            if strs[j][i] != strs[j+1][i]:
                break
    return retvalue

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
