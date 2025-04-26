import numpy as np

number_of_classes = np.array([[1, 2, 3,4],
                              [5,6,7,8],
                              [12,4,5,6]])
print(number_of_classes)


boys =  np.ones([3,4])
print(boys)

result = number_of_classes + boys 
print(result)

half = boys / 2
print(half)


different_dimension = np.full([1,4],2)

add_diff_dims = number_of_classes + different_dimension
print(add_diff_dims)


arr1 = np.array([[1,2,3],[2,3,4],[6,7,8]])
arr2 = np.array([[4,5,3],[2,8,9],[6,7,8]])

print(arr1 == arr2)