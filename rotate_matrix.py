

def rotate_matrix(grid):
    n = len(grid)
    for r in range(n//2):
        for c in range(n//2):
            left = 3

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
    rotate_matrix(matrix)
    print(matrix)