import random

class BogoSort:

    def __init__(self,nums):
        self.nums = nums


    def sort(self):
        
        #if sorted is not equal to true

        while not self.is_sorted():
            #shuffle the underlying dats structure
            print('Shuffle again....')
            self.shuffle()


    # Fisher-Yates approach : we generate new permutations in o(N)
    # it is in place so doesnot need aditional memory
    def shuffle(self):
        for i in range(len(self.nums)-2,0,-1):
            j = random.randint(0,i+1)
            self.nums[i],self.nums[j] = self.nums[j] , self.nums[i]




    def is_sorted(self):
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                #return false if underlying data structure is not sorted
                return False


        return True


if __name__ == '__main__':

    # it has o(n!) 
    algorithm = BogoSort([1,-4,5,8,2,3,0,-7])
    algorithm.sort()
    print(algorithm.nums)
