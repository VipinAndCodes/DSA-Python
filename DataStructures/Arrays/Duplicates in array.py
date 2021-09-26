# The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) running time where the
# integer values are smaller than the length of the array!
#
# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm can detect that there are a duplicate with value 1.
#
# Note: the array can not contain items smaller than 0 and items with values greater than the size of the list.
# This is how we can achieve O(N) linear running time complexity!


def find_duplicates(nums):

    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('Repitation found: %s' % str(abs(num)))

#This method cannot handle values < 0
#the max items is smaller than the size of the list
n = [2,6,5,1,4,3,2,6]

print(find_duplicates(n))

