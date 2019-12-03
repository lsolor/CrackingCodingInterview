

def helper(n, cache):
    if n <= 1:
        return 1

    if cache[n]!= 0:
        return cache[n]

    ans = 0

    for i in range(n):
        ans += helper(i, cache) * helper(n-i, cache)

    cache[n] = ans
    return cache[n]


def unique_bst(n):
    cache = [0] * (n + 1)

    return helper(n, cache)


if __name__ == '__main__':
    print(unique_bst(2))