def diving_board(shorter, longer, k):
    if k == 0:
        return 0
    if shorter < longer:
        temp = shorter
        shorter = longer
        longer = temp

    diff_lengths = []

    for i in range(k+1):
        diff_lengths.append(i * shorter + (k-i) * longer)

    print(diff_lengths)


if __name__ == '__main__':
    diving_board(2, 5, 4)
