class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # if a number is repeating more than once in an array, thats the answer
        
        # first approach - using for each number if it is occuring again, O(n2)
        # second approach - creating a frequency dict
        
        # ----------code ---------------------------------
        
#         frequency_dict = dict()
        
#         # iterating through all the elements of the array and counting their occurence
#         for num in nums:
#             if num not in frequency_dict:
#                 frequency_dict[num] = 1  # if num not in dict, assigning it 1
#             else:
#                 frequency_dict[num] += 1  # if already present, incrementing it
                
#         # print(frequency_dict)
#         # in the question, given that only one element is duplicate
#         # checking the dict
#         for key, value in frequency_dict.items():
#             if value > 1:
#                 return key

        # ----------- Binary Search Approach -------------------------#
#         low = 1
#         high = len(nums) - 1

#         while low <= high:
#             current = (low+high)//2
#             count = 0

#             # Count how many times are less than equal to current
#             for num in nums:
#                 if num <= current:
#                     count += 1
                    
#             if count > current:
#                 duplicate = current
#                 high = current - 1
#             else:
#                 low = current + 1

#         return duplicate

        # ---------------- Floyd's tortoise and Hare (cycle detection)---------------#
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        # Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return hare