def solve(word):
    vowels = "aeiou"
    consonant_substrings = ["".join(filter(lambda char: char not in vowels, word[i:])) for i in range(len(word))]
    values = [sum(ord(char) - ord('a') + 1 for char in substring) for substring in consonant_substrings]
    return max(values)

# Examples
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
