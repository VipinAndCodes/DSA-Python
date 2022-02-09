
class BubbleSort:

    def __init__(self,nums):
        self.nums = nums


    def sort(self):

        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j,j+1)


    def swap(self,i,j):
        self.nums[i],self.nums[j] = self.nums[j] , self.nums[i]



if __name__ == '__main__':

    # it has o(n!) 
    algorithm = BubbleSort([1,-4,5,8,2,3,0,-7])
    algorithm.sort()
    print(algorithm.nums)
