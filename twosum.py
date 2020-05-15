#Take an int array and return the two indices of numbers that add up to the target.
#Will there be repeating values? Will there be negative numbers?
#There will always be an answer.
#Brute force with a nested for loop could work
#A Hash-Table would be better, passing through twice to find the answer.

class Solution(): 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            j = lookup.get(complement)#hash table to search 
            if j != None and j != i: 
                return [i, j]
        return [] 
