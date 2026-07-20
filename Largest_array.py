# def largest(arr):
#     largest = arr[0]
#     n = len(arr)
#     for i in range(0,n):
#         largest = max(largest,arr[i])
#     return largest

# arr = [1,3,5,67,8,86,2]
# print(largest(arr))

def largest(arr):
    largest = arr[0]
    n = len(arr)
    for i in range (0,n):
        if arr[i]>largest :
            largest = arr[i]
    return largest 

arr = [1,3,5,67,8,86,2]
print(largest(arr))    
    