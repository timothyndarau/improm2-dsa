def remove_duplicates(sequence):
    seen = set()
    result = []
    
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

#test case bna
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5, 3, 2]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
