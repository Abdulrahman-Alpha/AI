import numpy as np
# # finding square roots 
# nums = [10 , 20 ,30, 40 ,50]
# np_sqr = np.sqrt(nums)
# print(np_sqr)
# #Finding Logs
# nums = [10,20,30,40,50] 
# np_log = np.log(nums) 
# print (np_log)
# #Finding Exponents
# nums = [10,20,30,40,50] 
# np_exp = np.exp(nums) 
# print (np_exp)
# #Finding Sine and Cosine
# nums = [10,20,30,40,50] 
# np_sine = np.sin(nums) 
# print (np_sine) 
# nums = [10,20,30,40,50] 
# np_cos = np.cos(nums) 
# print (np_cos)
# #Finding Matrix Dot Product
# #-To find a matrix dot product, you can use the dot() function. 
# #-To find the dot product, the number of columns in the first matrix must match the 
# #-number of rows in the second matrix.
# #-Script :
# A = np.random.randn(4,5) 
# B = np.random.randn(5,4) 
# Z = np.dot(A,B) 
# print (Z)
# #Element-wise Matrix Multiplication
# #-In addition to finding the dot product of two matrices, you can element-wise 
# #-multiply two matrices. 
# #-To do so, you can use the multiply() function. The dimensions of the two matrices 
# #-must match. 
# #-Script :
# row1 = [10,12,13] 
# row2 = [45,32,16] 
# row3 = [45,32,16] 
# nums_2d = np.array([row1, row2, row3]) 
# multiply = np.multiply(nums_2d, nums_2d) 
# print (multiply)
# #Finding Matrix Inverse
# #-You find the inverse of a matrix via the linalg.inv() function.
# #-Script :
# row1 = [1,2,3] 
# row2 = [4,5,6] 
# row3 = [7,8,9] 
# nums_2d = np.array([row1, row2, row3])
# inverse = np.linalg.inv(nums_2d) 
# print (inverse)
# #Finding Matrix Determinant
# #-Similarly, the determinant of a matrix can be found using the linalg.det() function.
# #-Script :
# row1 = [1,2,3] 
# row2 = [4,5,6]
# row3 = [7,8,9] 
# nums_2d = np.array([row1, row2, row3]) 
# determinant = np.linalg.det(nums_2d) 
# print (determinant)
# #Finding Matrix Trace
# #-The trace of a matrix refers to the sum of all the elements along the diagonal of a matrix. 
# #-To find the trace of a matrix, you can use the trace() function.
# #-Script :
row1 = [1,2,3] 
row2 = [4,5,6] 
row3 = [7,8,9] 
nums_2d = np.array([row1, row2, row3]) 
trace = np.trace(nums_2d) 
print (trace)