#universal function in numpy
#trigonomentric function
import numpy as np
A=np.array([1,2,3])
print("A:",A)
sin_value = np.sin(A)
print("A:",sin_value)


#Arithmetic functions
import numpy as np
a=np.array([1,3,4,6])
b=np.array([2,4,1,0])

addresult= np.add(a,b)
print("add result:",addresult)


#rounding functions
import numpy as np
v=np.array([1.2334,2.5632,3.7453])
rounded_array=np. round(v,2)
print("array after round :",rounded_array)


#statistical functions
import numpy as np
array1=np.array([1,2,3,4,5])
median=np.median(array1)
print("median :",median)
max=np.max(array1)
print("largest element is:",max)
