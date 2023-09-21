from collections import Counter

def sort_string_by_frequency(s):
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Sort the characters in the string by their frequency
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    
    # Build the final string by appending each character the number of times it appears in the original string
    result = ""
    for char in sorted_chars:
        result += char * freq[char]
    
    return result
