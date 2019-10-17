

def merge_sort(arr):
    temp = [0]*len(arr)
    count = merge_sort_helper(arr, temp, 0, len(arr)-1)
    print(arr)

def merge_sort_helper(arr, temp, left_start, right_end):
    # invalid array, which already sorted
    if left_start >= right_end:
        return 0

    middle = (left_start + right_end) // 2
    count = 0
    # sort left side
    count += merge_sort_helper(arr, temp, left_start, middle)

    # sort right side
    count += merge_sort_helper(arr, temp, middle + 1, right_end)
    count += merge(arr, temp, left_start, right_end)
    return count


def merge(arr, temp, left_start, right_end):
    count = 0
    left_end = (left_start + right_end)//2
    right_start = left_end + 1
    left = left_start
    right = right_start
    index = left_start

    last_taken = None
#both still in bounds
    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            temp[index] = arr[left]
            left += 1
            if(last_taken != None and last_taken == 'right'):
                last_taken = 'left'
                count += 1
            elif(last_taken == None):
                last_taken ='left'
        else:
            temp[index] = arr[right]
            right += 1
            if(last_taken != None and last_taken == 'left'):
                last_taken = 'right'
                count += 1
            elif (last_taken == None):
                last_taken = 'right'

        index += 1

    # copy rest into the array
    for i in range(left, left_end+1):
        temp[index] = arr[i]
        index += 1
    for j in range(right, right_end + 1):
        temp[index] = arr[j]
        index += 1

    # copy temp into array
    for k in range(left_start, right_end + 1):
        arr[k] = temp[k]
    return count


if __name__ == '__main__':
    arr = [3,4,2,76]
    merge_sort(arr)