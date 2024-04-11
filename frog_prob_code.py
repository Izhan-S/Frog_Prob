from collections import deque

def is_valid_move(state, from_pos, to_pos):

    if to_pos < 0 or to_pos >= len(state):
        return False 
    if state[to_pos] != '0':
        return False  
    if abs(from_pos - to_pos) > 1 and state[(from_pos + to_pos) // 2] == state[from_pos]:
        return False  # Can't jump over a frog of the same color
    return True

def generate_moves(state):
   
    moves = []
    for i, s in enumerate(state):
        if s == '2':  # Green frog can move to the right
            if i + 1 < len(state) and is_valid_move(state, i, i + 1):
                new_state = state[:i] + '0' + '2' + state[i+2:]
                print(f"Legal move: {state} -> {new_state}")
                moves.append(new_state)
            if i + 2 < len(state) and is_valid_move(state, i, i + 2):
                new_state = state[:i] + '0' + state[i+1:i+2] + '2' + state[i+3:]
                print(f"Legal move: {state} -> {new_state}")
                moves.append(new_state)
        elif s == '1':  # Red frog can move to the left
            if i - 1 >= 0 and is_valid_move(state, i, i - 1):
                new_state = state[:i-1] + '1' + '0' + state[i+1:]
                print(f"Legal move: {state} -> {new_state}")
                moves.append(new_state)
            if i - 2 >= 0 and is_valid_move(state, i, i - 2):
                new_state = state[:i-2] + '1' + state[i-1:i] + '0' + state[i+1:]
                print(f"Legal move: {state} -> {new_state}")
                moves.append(new_state)
    return moves

def bfs(start, goal):
    """Breadth-first search to explore all possible states."""
    queue = deque([start])
    visited = set([start])
    count = 0  
    while queue:
        current_state = queue.popleft()
        count += 1 

        for next_state in generate_moves(current_state):
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)

    return count, visited

# Initial and goal states
start_state = '2220111'
goal_state = '1110222'

count, states = bfs(start_state, goal_state)

# Print the total number of states
print(f"Total number of states: {count}")
