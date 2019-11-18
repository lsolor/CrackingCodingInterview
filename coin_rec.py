def coins(n):
    cache = [0] * (n + 1)
    cache[0] = 1
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    cache[4] = 1

    cache_helper(n, cache)
    print(cache)
    return


def cache_helper(n, cache):
    if cache[n] != 0:
        return cache[n]
    print("on %d" %n)

    nickel = 0
    dime = 0
    quarter = 0
    if n-5 >= 0:
        nickel = cache_helper(n-5, cache)
        print('add 5')
    if n-10 >= 0:
        dime = cache_helper(n-10, cache)
    if n-25 >= 0:
        quarter = cache_helper(n-25, cache)
    cache[n] = 1 + nickel + dime + quarter
    return cache[n]

if __name__ == '__main__':
    print(coins(26))