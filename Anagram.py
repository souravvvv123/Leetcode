def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


print(is_anagram("triangle", "integral"))  # Output: True
print(is_anagram("apple", "pale"))  # Output: False




