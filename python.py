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

# def generate(numRows): 
#     result=[] #making a empty list
#     for i in range(numRows): #loop through rows 
#         print("this is i index number",i)
#         result.append([]) #and add empe
#         # print("this is result",result)
#         for j in range(i+1):# there are "i" elements in each row and loop start from 0, so should be end at i+1
#             print("2nd loop Print: i = ",i)
#             print("this is j",j)
#             if j in (0,i):
#                 result[i].append(1)
#             else:
#                 result[i].append(result[i-1][j-1] + result[i-1][j])
#         print("result: ",result)
#         print("")

    # return result
# print(generate(numsRows))

# 119 pascal's triangle
numsRows = 3

def generate(rows):
    result = [1]+[0]*rows
    for i in range(rows):
        for j in range(i+1,0,-1):#stop at 0 , so 0 index in not included
            result[j]=result[j]+result[j-1]
    return result
print(generate(numsRows))

# # result[i][j] = result[i][j-1]+ result[i][j+1]

#      [1],
#     [1,1],
#    [1,2,1],result[i][1] = result[i][j-1]+ result[i][j+1]
#   [1,2,2,1],result[i][2] = result[i][j-1]+ result[i][j+1]
#  [1,2,2,1,1],result[i][3] = result[i][j-1]+ result[i][j+1]

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





# from typing import List
# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# nums = [1,2,3,4]

# def revers(any):
#     new_list = any[::-1]
#     return new_list
# print(revers(nums))
# def rungsum(listNums):
#     for i in range(1,len(listNums)):
#         listNums[i]=listNums[i]+listNums[i-1]
#         #   3+1=4
#         #   4+2 = 6
#         #   6+4 = 10
#     return listNums
# print(rungsum(nums))






# 1431. Kids With the Greatest Number of Candies
# candies = [2,3,5,1,3]

# max(candies)
# print




# 189. Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
 
# nums = [1,2,3, 4,5,6,7] nums[:k] nums[:k]
#         5,6,7，  1,2,3,4 nums[len(nums-k：)]
# k = 3
# k就是indexnumber
# # Output: [5,6,7,1,2,3,4]
# # Explanation:
# # rotate 1 steps to the right: [7,1,2,3,4,5,6]
# # rotate 2 steps to the right: [6,7,1,2,3,4,5]
# # rotate 3 steps to the right: [5,6,7,1,2,3,4]
# # We can switch a group of nums end at 3rd number with the nums start from index 4 and end at the last number

# # 把数组的后三位数移动到前三位，或者说把这个数组向右推进三次
# # 1,2,3     4,5,6,7
# # 5,6,7     1,2,3,4  
# # 第一步先求余数， 因为如果给出的数是11，那么就是说要推进11次。也就是说只要知道它的余数旧能知道有效推进的结果。
# k = k % len(nums)
# # 第二部, 从头到第K个数，和K个数之后的数进行调换。

# nums[:k] , nums[k:] = nums[len(nums)-k:] , nums[: len(nums)-k:]
# 1，2，3    4，5，6，7 =      5，6，7              1，2，3，4
# print(nums[len(nums)-k:])
# print(nums[:k])
# print(nums[k:])

