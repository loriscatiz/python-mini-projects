def lengthOfLongestSubstring(s: str) -> int:
    longest = ''
    candidates :list[str] = []
    i = 0
    while i < len(s):
        if not s[i] in longest:
            longest += s[i]
        else:
            candidates.append(longest)
            longest = longest.replace(longest[0], '')
            i-=1
        i+=1
    candidates.append(longest)
    return len(max(candidates, key=len))

print(lengthOfLongestSubstring('dvdf'))