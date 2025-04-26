import numpy as np

# array1 = np.arange(1,7).reshape(3,2)
# print(array1)


# array2 = np.zeros(6).reshape(3,2)  # reshape array using row and column
# print(array2)

# list1 = [1,2,3,4,5,6]
# array3 = np.array(list1)           # Similar  data type list
# print(array3)

# list2 = [1,2,3,4.9,5,6]
# array4 = np.array(list2)           # Different data type list
# print(array4)

# list3 = [1,2,3,4,'hello',5,6]
# array5 = np.array(list3)           # Non-numeric data type list
# print(array5)


# list4 = [1,2,3.4,'hello',5,6]
# array6 = np.array(list4, dtype=object)  # Different data type list with dtype=object
# print(array6)

# list5 =[1,2,3,4]
# array7 = np.array(list5, dtype=float)    # Different data type list
# print(array7)

# list6 = [1,2,3.4,'hello',5.6,True]
# array8 = np.array(list6)                 # Different data type list
# print(array8)


#----------------------------------------
# Class work:

# even = np.arange(0,10,2)              # intialize with even
# odd = np.arange(1,10,2)            # intialize with odd

# print(even,odd)


# sh =  even.shape
# print(sh)

# arr3 = np.random.randint(0,100,[2,3,4])
# print(arr3)


# students = np.random.randint(0,80,[1000,3])
# print(students.shape)
# print(students)


# a = np.linspace(2,16,8)
# print(a)
# re_a = a.reshape(2,4)
# print(re_a)

# arr1 = np.arange(5,8)
# print(arr1)

# arr1 = np.array([1,2,3])

# for x in arr1:
#     print(type(x))

# arr3 = np.array([[11, 12, 13, 14],
#     [15, 16, 17, 18],
#     [19, 11, 12, 13]])
# print(arr3.shape)


# arr4 = np.zeros((3, 2))
# print(arr4)

# arr5 = np.ones((4, 4))
# print(arr5)

# arr3 = np.ones([2, 2, 3])
# print(arr3)

# arr6 = np.eye(5)
# print(arr6)