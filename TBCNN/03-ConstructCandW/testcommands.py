import numpy as np
# intarr= [0,1,2,3,4,5]
# a= np.reshape(intarr, (2, 3)) # C-like index ordering
# print a
# a = np.reshape(intarr, (2, 3), order='A') # equivalent to C ravel then C reshape
# print a
# a = np.reshape(intarr, (2, 3), order='F') # Fortran-like index ordering
# print a
# a = np.reshape(intarr, (-1,2)) # Fortran-like index ordering
# print a
# print intarr
# import parser
# text =""
# ast = parser.parse(text=text)
numFea = 4
w1 = (np.eye(numFea) / 2)
print w1
w1 = w1.reshape(-1)
print w1