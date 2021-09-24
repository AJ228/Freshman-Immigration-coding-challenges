class Solution(object):
    def twoSum(self, nums, target):
        #Challenge parameters
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = [] #Blank list to store answer indices
        for i in range (len(nums)-1): #Checks all combinations from nums
            for j in range(len(nums)):
                if i != j: #Makes sure element indices are not identical
                    if nums[i] + nums[j] == target: #Appends indices to answer if numbers add to target
                        answer.append(i)
                        answer.append(j)
            if len(answer) == 2: #Stops running once answer has two elements
                break
        return(answer)
#Testing if code works properly
solution = Solution()
print("Testing twoSum()...",end="")
assert(solution.twoSum([2,7,11,15],9) == [0,1])
assert(solution.twoSum([3,2,4],6) == [1,2])
assert(solution.twoSum([3,3],6) == [0,1])
assert(solution.twoSum([2,7,11,15],22) == [1,3])
print("Passed!")