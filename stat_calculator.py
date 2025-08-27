import numpy as np

numbers= input("Enter numbers seperated by spaces: ")
data=np.array([float(x) for x in numbers.split()])

mean_value= np.mean(data)
median_value= np.median(data)
std_deviation= np.std(data)
variance_value= np.var(data)

print("-------------------------Statistical Data----------------------------")
print(f"Data: {data}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Variance: {variance_value}")
print(f"Standard deviation: {std_deviation}")