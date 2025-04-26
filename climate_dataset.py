import numpy as np

climate_data = np.genfromtxt('dataset analysis/climate.txt',delimiter = ',', dtype=float,skip_header=1)
print(climate_data)

print(climate_data.shape)


weights = np.array([0.3,0.2,0.5])

yeild = climate_data@weights
print(yeild)


yeild2 = np.dot(climate_data, weights)
print(yeild2.reshape(10000,1))


climate_results = np.concatenate((climate_data,yeild.reshape(10000,1)),axis = 1)
print(climate_results)


np.savetxt('dataset analysis/climate_results.txt', 
           climate_results, 
           delimiter='|',
           comments='this is the result: ' , 
           fmt='%0f')                           # %d = save as txt ,  %(int)f = save as float with (int) decimal points.



mean = np.mean(weights)
print('this is mean', mean)


std_dev = np.std(weights)
print('this is standard deviation', std_dev)


# mode = np.mod(weights)
# print('this is mode', mode)


median = np.median(weights)
print('this is median', median)



hot_days = climate_data[climate_data : 0 > 30]
print('thses are hot days', hot_days)