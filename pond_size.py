import queue

def BFS(matrix, starting_r, starting_c, visited):
    q = queue.Queue()
    size = 0
    q.put((starting_r,starting_c))
    visited.add((starting_r,starting_c))

    while not q.empty():
        current = q.get()
        size += 1

        for r in range(-1,2):
            for c in range(-1,2):
                neighbor_r = r + current[0]
                neighbor_c = c + current[1]
                if 0 <= neighbor_r < len(matrix) and 0 <= neighbor_c < len(matrix) and (neighbor_r, neighbor_c) not in visited and matrix[neighbor_r][neighbor_c] == 0:
                    q.put((neighbor_r,neighbor_c))
                    visited.add((neighbor_r, neighbor_c))
    return size


def pond_size(matrix):
    sizes = []
    visited = set()

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 0 and (r,c) not in visited:
                sizes.append(BFS(matrix, r, c, visited))

    for i in range(len(sizes)):
        print(sizes[i], end=",")


if __name__ == '__main__':
    test = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
    pond_size(test)
