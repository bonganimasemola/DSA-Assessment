def remove_duplicates(sequence):
    """
    Function to remove duplicate elements from a given sequence.

    Parameters:
        sequence (list or tuple): Sequence from which duplicate elements need to be removed.

    Returns:
        list: Sequence with duplicate elements removed.
    """
     # Initialize an empty tuple to store the seen elements
    seen = ()
     # Initialize an empty list to store the result sequence
    result = []
     # Iterate through each element in the input sequence
    for item in sequence:
        
        # If the current element is not present in the seen tuple,
        # add it to the seen tuple and the result list
        if item not in seen:
            # seen.add(item)
            result.append(item)
            seen += (item,)
            
     # Return the sequence with duplicate elements removed
    return result 


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 