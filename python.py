# nums = [-2,1,-3,4,-1,2,1,-5,4]

# def  maxSubArray(nums):
#     if max(nums)<0:
#         return max(nums)
    
#     local_max, global_max = 0 , 0
#     for num in nums:
#         local_max = max(0,local_max+num)
#         global_max= max(global_max,local_max)
    
#     return global_max

# print(maxSubArray(nums))
# print('HelloWorld123')

# 118 pascal's Triangle
# numsRows = 3

# def generate(rows):
#     result=[]
#     for i in range(rows):
#         result.append([])
#         for j in range(i+1):
#             if j in (0,i):
#                  result[i].append(1)
#             else:
#                 result[i].append(result[i-1][j-1] + result[i-1][j])
#     return result
# print(generate(numsRows))

# 119 pascal's triangle
# numsRows = 3

# def generate(rows):
#     result = [1]+[0]*rows
#     for i in range(rows):
#         for j in range(i+1,0,-1):
#             result[j]=result[j]+result[j-1]
    
#     return result
# print(generate(numsRows))
# class Solution:
#     s = 'IV'
#     def romanToInt(self, s: str) -> int:
#         numeral_map={
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000
#         }
#         result = 0 
#         for i in range(len(s)):
#             if i >0 and numeral_map[s[i]]>numeral_map[s[i-1]]:
#                 result+=numeral_map[s[i]]-2*numeral_map[s[i-1]]
#             else:
#                 result += numeral_map[s[i]]
#         return result
#     print(romanToInt(s))

# Longest Common Prefix
# def longestCommonPrefix(self, strs: List[str]) -> str:
#     result = ''
#     i=0
    
#     while True:
#         try:
#             sets=set(string[i] for string in strs)
#             if len(sets) == 1 :
#                 result += sets.pop()
#                 i+=1
#             else: 
#                 break
#         except Exception as e:
#             break

# LeetCode in Python 122. Best Time to Buy and Sell Stock II 
# prices = [1,2,3,4,5]
# # output 4
# def maxProfit(nums):
#     if len(nums)<=1:
#         return 0
    
#     total=0
#     for i in range(1,len(nums)):#从因为要用当前和之前（i-1）位作比较
#         if nums[i]>nums[i-1]:
#             total +=nums[i]-nums[i-1]
#     return total
# print(maxProfit(prices))

#162 Find Pick Element
# nums=[1,2,1,3,5,6,4]
# #output index 1 or 5
# def findPickElement(nms):
#     left, right = 0,len(nms)-1
#     while left < right:
#         mid = (left+right)//2
#         if nms[mid] < nms[mid+1]:
#             left=mid+1
#         else:
#             right=mid
#     return left
# print(findPickElement(nums))

#leetcode 167 Two sum II
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Note:

# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# numbers = [2,7,11,15]
# target = 9
# def twoSumsII(list, targetnum):
#     start,end = 0,len(list)-1
#     sum = 0 
#     while start != end :
#         sum = list[start]+list[end]
#         if sum>targetnum:
#             end-=1
#         elif sum<targetnum:
#             start+=1
#         else:
#             return start+1, end+1
# print(twoSumsII(numbers,target))