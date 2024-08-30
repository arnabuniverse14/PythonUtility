'''Write a Python program that calculates the average of a list of numbers.
In:  [5, 10, 15, 20]
Out:  12.5
If the list is empty, return 0'''

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # To handle an empty list and avoid division by zero
        
    total = sum(numbers)
    average = total / len(numbers)
    return average 
    
lst = [5, 10, 15, 20] 
average = calculate_average(lst)

print("Average of the list =", average)
