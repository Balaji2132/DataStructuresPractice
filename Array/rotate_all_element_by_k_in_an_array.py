def rotate_array (arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

n = int(input("Enter the number of elemnts in the array: "))
array = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

k = int(input("Enter the value of k: "))
rotated_array = rotate_array(array, k)
print("Rotated array is: ", rotated_array)