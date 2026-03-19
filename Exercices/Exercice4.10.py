def substring_length(string):
    if not string:
        return ""
    
    max_substring = ""
    
    for i in range(len(string)):
        current = ""
        seen = set()
        
        for j in range(i, len(string)):
            if string[j] in seen:
                break
            current += string[j]
            seen.add(string[j])
        
        if len(current) > len(max_substring):
            max_substring = current
    
    return max_substring

print(substring_length("abcabcbb"))
print(substring_length("bbbbb"))
print(substring_length("pwwkew"))