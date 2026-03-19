def count_compressing(string):
    if not string:
        return ""
    
    b_char = string[0]
    counter = 1
    text = ""
    
    for char in string[1:]:
        if char == b_char:
            counter += 1
        else:
            text += b_char + str(counter)
            b_char = char
            counter = 1

    text += b_char + str(counter)
    
    return text

print(count_compressing("aabbcccc"))
print(count_compressing("aaabbbcccaaa"))
print(count_compressing("abcdef"))