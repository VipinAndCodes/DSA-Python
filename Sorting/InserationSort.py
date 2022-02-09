
def insertion_sort(nums):


    for i in range(len(nums)):


        j=i


        #we have to check all the previous items(not always all of them)
        #worst case we consider all the previous items
        while j>0 and nums[j-1] > nums[j]:
        #for descending order
        #while j>0 and nums[j-1] < nums[j]:
            #swap the items - shift operations
            #this is main disadvantage of insertion sort O(n*n)

            nums[j-1] , nums[j] = nums[j],nums[j-1]

            j = j-1


if __name__ == '__main__':

    # it has o(n!) 
    n = [1,-4,5,8,2,3,0,-7]
    insertion_sort(n)
    print(n)
