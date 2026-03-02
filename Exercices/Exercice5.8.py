def extract_even_sequence(sequence):
    return sequence[::2]

# def extract_even_sequence(sequence):
#     return [item for i, item in enumerate(sequence) if i % 2 == 0]

print(extract_even_sequence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))