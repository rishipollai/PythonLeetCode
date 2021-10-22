class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces_dict = {}
        for index,number in enumerate(nums):
            if target-number in indeces_dict:
                return [indeces_dict[target-number],index]
            indeces_dict[number]=index
