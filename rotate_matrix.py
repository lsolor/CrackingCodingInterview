def coins(n):
    cache = [0] * (n + 1)
    cache[0] = 1
    cache_helper(n, cache)
    print(cache)
    return


def cache_helper(n, cache):
    if cache[n] != 0:
        return cache[n]
    print("on %d" %n)
    if n-1 >= 0:
        print('add 1')
        cache[n] += cache_helper(n-1, cache)
    if n-5 >= 0:
        cache[n] += cache_helper(n-5, cache)
        print('add 5')
    if n-10 >= 0:
        cache[n] += cache_helper(n-10, cache)
    if n-25 >= 0:
        cache[n] += cache_helper(n-25, cache)
    return cache[n]

if __name__ == '__main__':
    print(coins(6))