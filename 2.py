def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])