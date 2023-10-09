def linear_search(val, arr):
    for i in range (0, len(arr)):
        if arr[i] == val: 
            print(i)
            return i
    print(None)
    return None
        
linear_search(5, [4, 5, 4, 3, 4, 3, 2])

def linear_search_global(val, arr):
    all_indices = []
    for i in range(0, len(arr)): 
        if arr[i] == val:
            all_indices.append(i)
    if all_indices == []:
        print (None)
        return None
    else: 
        print (all_indices)
        return all_indices
linear_search_global(4, [2, 4, 5, 6, 4, 3, 5, 4, 5, 4])

   