from re import I


def shell_sort(nums):


    gap = len(nums)//2



    # this is the shell sort

    while gap > 0 :


        #this is the same as nsertion sort but here we have to consider
        #items that are as far away from each other as the value of the 'gap'
        for i in range(gap,len(nums)):

            j = i

            while j>= gap  and nums[j-gap] > nums[j]:
                nums[j], nums[j - gap] = nums[j-gap],nums[j]
                j = j - gap


        gap = gap // 2


if __name__ == '__main__':

    # it has o(n!) 
    n = [1,-4,5,8,2,3,0,-7]
    shell_sort(n)
    print(n)


