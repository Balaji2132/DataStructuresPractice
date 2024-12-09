def reverse_array(arr):
    return arr[::-1]

def find_second_largest (arr):
    unique_numbers = list(set(arr))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

n = int(input("Enter the number of elements in tha array: "))
array = []
for i in range (n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

reversed_array = reverse_array(array)
print("Reversed array:", reversed_array)
second_largest = find_second_largest(reversed_array)
if second_largest is not None:
    print("Second largest element in the array:", second_largest)
else:
    print("There is no second largest element in the array.")