my_pets = ['alfred', 'tabitha', 'william', 'arla']
print(list(map(lambda x : x.upper(),my_pets)))

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(lambda x : round(x),circle_areas[0:2]))
print(result)

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

#Give the output without executing the code
print(python_list + python_list) #Ans: [1,2,3,1,2,3]
print('\n')
print(numpy_array + numpy_array) #Ans: [2,4,6]

import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 100), 2)
weight = np.round(np.random.normal(60.32, 15, 100), 2)
#numpy.random.normal(loc = 0.0, scale = 1.0, size = None)
#creating a normal distribution here with 1.75 as mean, sd of 0.20 of normal deviation ,100 as size.(100 entries)
#also rounds all these entries to float with 2 places after decimal
#same applies for weight
BMI = (weight)/(height*height)
#wonders of numpy

foo = np.arange(11,20)
foo = np.arange(11,20).resize(3,3)
print("3x3 Matrix of foo = \n{}\n".format(foo))
#the wonders

a = np.array([(1,2,3),(4,5,6)])
b = np.arange(11, 20).reshape(3, -1)
#why the -1 even though 3*3 matrix gets printed
zero_line = np.zeros((1,3))
#y is it 0 with float

c = np.concatenate((a,b,zero_line))

print("c = np.vstack((a,b, zero_line)) = \n{}\n".format(c))

#last question
xint = input()
intlist = list(map(lambda x : int(x),xint.split(" ")))
arr = np.array(intlist).astype(float)
print(arr)
