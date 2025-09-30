from collections import deque
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solve_puzzle(start):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if state == goal_state:
            return path + [state]
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                queue.append((new_state, path + [state]))
    return None
solution = solve_puzzle(initial_state)
if solution:
    print(f"Solution found in {len(solution)-1} moves:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists!")