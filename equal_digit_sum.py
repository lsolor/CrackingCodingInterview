# given an array A consisting of N integers, return
# the maximum sum of two numbers whose digits add
# up to an equal sum. If there are no two numbers whose
# digits have an equal sum, the function should return -1
# ex A = [51, 71, 17, 42] return 93 which is the sum of (51 and 42)

def equal_digit_sum(A):
    digit_sum = {}

    for num in A:
        val = get_digit_sum(num)
        if val in digit_sum:
            digit_sum[val].append(num)
        else:
            digit_sum[val] = [num]

    max_digit_sum = -1

    for arr, v in digit_sum.items():
        print(v)
        if len(v) > 1:
            tup = get_two(v)
            max_digit_sum = max(max_digit_sum, (tup[0] + tup[1]))

    return max_digit_sum


def get_two(arr):
    first = 0
    second = 0

    for i in arr:
        if i > first:
            second = first
            first = i
        elif i> second:
            second = i
    return (first, second)


def get_digit_sum(num):
    res = 0

    while num:
        res += num % 10
        num = num // 10

    return res

if __name__ == '__main__':
    A = [51, 71, 17, 42]
    B = [51, 43, 22]
    print(equal_digit_sum(A))
    print(equal_digit_sum(B))