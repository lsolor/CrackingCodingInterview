
def sum_swap(arr_a, arr_b):
    if len(arr_b) > len(arr_a):
        return sum_swap(arr_b, arr_a)

    s = set()

    a_sum = 0
    b_sum = 0
    for i in arr_a:
        s.add(i)
        a_sum += i

    for j in arr_b:
        b_sum += j

    for num in arr_b:
        temp_a_sum = a_sum + num
        temp_b_sum = b_sum - num
        diff = abs(temp_a_sum - temp_b_sum)
        if diff/2 in s:
            print("%d and %d" %(num, diff/2))
            return
    print("no value possible")


if __name__ == '__main__':
    arr = [4, 1, 2, 1, 1, 5]
    arr_2 = [7, 5, 1, 4, 4]

    sum_swap(arr, arr_2)


