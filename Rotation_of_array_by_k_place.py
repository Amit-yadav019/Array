# def rotation_by_k_place(arr):
#     n = len(arr)
#     for i in range(0,k):
#         arr[:] = arr[1:n] + arr[0:1]
#     return arr
# k = int(input("enter the values of K for which place you want to Rotates : "))
# arr = [3,9,5,6,7,2,5,8]
# print(f"the left rotataion of an array{arr} by {k} place is ",rotation_by_k_place(arr))    


# now common and alternate approach 

    

# Better soln. 
def rotation_by_k_place(arr,k):
    n = len(arr)
    k = k%n
    
    arr[:] = arr[k: ] + arr[ :k]
    return arr
k = int(input("enter the values of K for which place you want to Rotates : "))

arr = [3,9,5,6,7,2,5,8]
print(f"the left rotataion of an array{arr} by {k} place is ",rotation_by_k_place(arr,k))  