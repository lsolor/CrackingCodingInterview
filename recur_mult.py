

def recur_mult(a,b):
    if a < b:
        return recur_mult(b, a)
    cache = [0] * (b+1)
    helper(a, b, cache)
    return cache[b]


def helper(a, b, cache):
    if b == 1:
        return a
    if cache[b] != 0:
        return cache[b]

    if b%2 == 0:
        ans = helper(a, b//2, cache) + helper(a, b//2, cache)
    else:
        ans = helper(a, b // 2, cache) + helper(a, b // 2, cache) + a

    cache[b] = ans
    return cache[b]


if __name__ == '__main__':
    print(recur_mult(21, 7))
