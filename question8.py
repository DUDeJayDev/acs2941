# Given a string, find the length of the longest non-repeating substring.

def find_longest_substring(text):
    longest = 0
    index = 0
    mapping = {}

    for i, char in enumerate(text):
        if char in mapping and mapping[char] >= index:
            index = max(index, mapping[char] + 1)
        longest = max(longest, i - index + 1)
        mapping[char] = i

    return longest


print(find_longest_substring("abcabcbb"))
print(find_longest_substring("bbbbb"))
print(find_longest_substring("pwwkew"))
