def recursive_binarysearch(list,target):
    if len(list) ==0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint]==target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binarysearch(list[midpoint+1:],target)
            else:
                return recursive_binarysearch(list[:midpoint],target)


def verify(result):
    print("Target found",result)

numbers = [item for item in range(0,11)]

print(numbers)

result = recursive_binarysearch(numbers,20)

verify(result)