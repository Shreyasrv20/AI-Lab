start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
def get_neighbors(state):
    neighbors = []
    pos = state.index(0)
    moves = [-3, 3, -1, 1]
    for move in moves:
        new_pos = pos + move
        if 0 <= new_pos < 9:
            if move == -1 and pos % 3 == 0:
                continue
            if move == 1 and pos % 3 == 2:
                continue
            new_state = list(state)
            new_state[pos], new_state[new_pos] = (
                new_state[new_pos], new_state[pos]
            )
            neighbors.append(tuple(new_state))
    return neighbors
def dls(state, depth, path, visited):
    if state == goal:
        return path
    if depth == 0:
        return None
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = dls(
                neighbor,
                depth - 1,
                path + [neighbor],
                visited | {neighbor}
            )
            if result is not None:
                return result
    return None
def ids(start):
    for depth in range(50):
        result = dls(start, depth, [start], {start})
        if result is not None:
            return result
    return None
solution = ids(start)
if solution:
    print("Goal State Found!")
    print("Number of moves:", len(solution) - 1)
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("Solution not found")
