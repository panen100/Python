arr = [1,20,33,45,50,66]
target = 100

def binary_search(_arr,_target):
    left = 0
    right = len(_arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if _arr[mid] == _target:
            return mid
        elif _arr[mid] > _target:
            right = mid + 1
        elif _arr[mid] < _target:
            left = mid + 1
    return -1
    
result = binary_search(arr,target)
print(result)
