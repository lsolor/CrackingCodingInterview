
def circus_sort(arr):
    n = len(arr)

    cache = [0] * n
    cache[0] = 1
    arr.sort()

    for i in range(1, n):
        greatest = 0
        for j in range(i, -1, -1):
            if arr[j][1] < arr[i][1]:
                greatest = max(greatest, cache[j])
        cache[i] = greatest + 1

    return max(cache)


if __name__ == '__main__':
    n = [(65,100), (70, 150), (56,90), (75,190), (60,95), (68,110)]
    print(circus_sort(n))