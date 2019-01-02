class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## SOLUTION - 1
        # for i in range(len(nums)):
            # curr_num = nums[i]
            # curr_index = i
            # for j in range(i+1, len(nums)):
                # second_num = nums[j]
                # if curr_num+second_num == target:
                    # return [curr_index, j]
                    
        hashTable = {}
        for _index, value in enumerate(nums):
            if not value in hashTable:
                hashTable[value] = _index
            if target-value in hashTable:
                if _index != hashTable[target-value]:
                    return [hashTable[target-value], _index]
        return None
                    
if __name__=='__main__':
    solution = Solution()
    print solution.twoSum(nums=[2, 7, 8, 1], target=9)
        