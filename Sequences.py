def remove_duplicates(sequence):
    """
    create a new list and iterating through the elements of the input sequence while adding each unique element to the new list
    """
    
    seen = ()
    result = []
    
    for item in sequence:
        if item not in seen:
            # seen.add(item)
            result.append(item)
            seen += (item,)
    return result 


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 