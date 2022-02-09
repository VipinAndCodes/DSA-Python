from turtle import right


def merge_sort(nums):


    #define the base case: that we keep spliting the list untill the
    #sublist have just 1 item - arrays with a single item is sorted by deafult

    if len(nums) == 1:
        return

    #DIVIDE PHASE

    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    #call merge sort recursivley left and right half
    merge_sort(left_half)
    merge_sort(right_half)

    # CONQUER PHASE

    i=0
    j=0
    k=0

    while i<len(left_half) and j<len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i = i + 1

        else:
            nums[k] = right_half[j]
            j = j + 1

        
        k = k + 1 

    #after that there may be additional items in right or left subarrays

    while i < len(left_half):
        nums[k] = left_half[i]
        i= i + 1
        k = k + 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j= j + 1
        k = k + 1


if __name__ == '__main__':

    # it has o(n!) 
    n = [1,-4,5,8,2,3,0,-7]
    merge_sort(n)
    print(n)

    







