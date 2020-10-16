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
for i in range(5+1,0,-1):
    print(i)