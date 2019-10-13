import sys


def subsort(arr):
    greatest_seen = -sys.maxsize
    lowest_value = sys.maxsize

    for i in range(len(arr)):
        if arr[i] > greatest_seen:
            greatest_seen = arr[i]

        if i != 0:
            if arr[i] < greatest_seen:
                last_index = i
                if arr[i] < lowest_value:
                    lowest_value = arr[i]

    if lowest_value == sys.maxsize:
        print("already in order")
        return

    print(lowest_value)
    for j in range(len(arr)):
        if arr[j] > lowest_value:
            beg_index = j
            print(arr[j])
            print("(%d, %d)" % (beg_index, last_index))
            return


if __name__ == "__main__":
    arr = [1, 2, 3, 7, 10]
    subsort(arr)