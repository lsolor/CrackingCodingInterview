import sys

# returns a - b by only using the '+' operator
def operation_sub(a, b):
    if b == 0:
        return a
    # Get two's complement of b
    negated_b = ~b
    negated_b += 1
    return a + negated_b

def operation_mult(a, b):
    negative_a = False
    negative_b = False
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    if a < 0:
        a = operation_sub(0, a)
        negative_a = True
    if b< 0:
        b = operation_sub(0, b)
        negative_b = True

    little = min(a, b)
    big = max(a, b)
    total_sum = 0

    while little > 0:
        total_sum += big
        little = operation_sub(little, 1)

    if negative_a and negative_b:
        return total_sum
    elif negative_a or negative_b:
        return operation_sub(0, total_sum)
    else:
        return total_sum


def operation_div(a, b):
    negative_a = False
    negative_b = False
    if a < 0:
        a = operation_sub(0, a)
        negative_a = True
    if b< 0:
        b = operation_sub(0, b)
        negative_b = True
    total = 0
    i = 0
    while total + b <= a:
        total += b
        i += 1
    if negative_a and negative_b:
        return i
    elif negative_a or negative_b:
        return operation_sub(0, i)
    else:
        return i


if __name__ == '__main__':
    # print(operation_sub(4, -2))
    a = int (input("Give an A: "))
    b = int(input("Give a B: "))
    print(operation_div(a, b), end="")
