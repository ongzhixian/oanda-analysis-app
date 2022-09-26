import numpy as np

#Current state
I = np.matrix([
        [1, 0]
    ])

#Transition Matrix
T = np.matrix([
        [.7, 0.3],  # 
        [.6, 0.4]   #
    ])

T1 = I * T
# After 1 hours
print (T1)

T2 = T1 * T
# After 2 hours
print (T2)


T3 = T2 * T
# After 3 hours
print (T3)


# Reference: https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html#basic-slicing-and-indexing
# x = np.matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#          0    1   2    3
# matrix([[ 1,  2,  3,  4],   # 0
#         [ 5,  6,  7,  8],   # 1
#         [ 9, 10, 11, 12],   # 2
#         [13, 14, 15, 16]])  # 3
# >>> x[1:3]     # Select rows 1 to 2 ==> Syntax is really `[n:m)`
# matrix([[ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]])
# >>> x[1:3, 1:4]     # select [1:3) rows, [1:4) columns
# matrix([[ 6,  7,  8],
#         [10, 11, 12]])
        
# x[1:3,1:4]=np.matrix([[-1,-2,-3],[-4,-5,-6]])
# >>> x[1:3,1:4]=np.matrix([[-1,-2,-3],[-4,-5,-6]])
# >>> x 
# matrix([[ 1,  2,  3,  4],
#         [ 5, -1, -2, -3],
#         [ 9, -4, -5, -6],
#         [13, 14, 15, 16]])
# >>>

# Reference: https://medium.com/@balamurali_m/markov-chain-simple-example-with-python-985d33b14d19