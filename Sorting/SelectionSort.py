
def selection_sort(nums):

    # we make n-1 iterations

    for i in range(len(nums)-1):

        #linear search and the index stores the index of the min item
        index = i

        #This is the linear search
        for j in range(i, len(nums)):
            
            #for accending order
            # if nums[j] > nums[index]:
            #     index = j

            #for decending order
            if nums[index] < nums[j]:
                index = j



        #we have to swap the min item with the left-most item
        #we do not swap the item with iteself

        if index != i:
            nums[index],nums[i]=nums[i],nums[index]


if __name__ == '__main__':

    # it has o(n!) 
    n = [1,-4,5,8,2,3,0,-7]
    selection_sort(n)
    print(n)
