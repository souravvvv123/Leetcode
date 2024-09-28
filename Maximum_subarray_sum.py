arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = float('-inf')  #the lowest no


for i in range(len(arr)):
    for j in range(i, len(arr)):
        current_sum = 0
        for k in range(i, j + 1):
            current_sum += arr[k]
        max_sum = max(max_sum, current_sum)

print("Maximum subarray sum is:", max_sum)
