def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target value found at index:",index)
    else:
        print("Target not found in list")

numbers = [item for item in range(0,11)]

print(numbers)

result = linear_search(numbers,8)

verify(result)