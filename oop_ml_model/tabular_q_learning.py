import numpy as np

# --- CẤU HÌNH MÔI TRƯỜNG ---
SIZE = 5
MESSI_START = (0, 0)
GOAL = (4, 4)
DEFENDERS = [(1, 1), (2, 3), (3, 1), (4, 2)]
ACTIONS = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)] # Up, Down, Left, Right
NUM_ACTIONS = len(ACTIONS)

# Khởi tạo Q-Table (State: 5x5, Action: 4)
q_table = np.zeros((SIZE, SIZE, NUM_ACTIONS))

# Tham số học tập
alpha = 0.1   # Learning rate
gamma = 0.9   # Discount factor
epsilon = 0.1 # Exploration rate

def get_next_state(curr_state, action_idx):
    direction = ACTIONS[action_idx]
    next_r = max(0, min(SIZE - 1, curr_state[0] + direction[1]))
    next_c = max(0, min(SIZE - 1, curr_state[1] + direction[2]))
    next_state = (next_r, next_c)
    
    # Reward logic
    if next_state == GOAL:
        return next_state, 10, True
    if next_state in DEFENDERS:
        return next_state, -10, True
    return next_state, -1, False

# --- TRAINING (Đơn giản hóa) ---
for episode in range(1000):
    curr = MESSI_START
    done = False
    while not done:
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.randint(NUM_ACTIONS)
        else:
            action = np.argmax(q_table[curr[0], curr[1]])
        
        next_s, reward, done = get_next_state(curr, action)
        
        # Cập nhật Q-value
        old_value = q_table[curr[0], curr[1], action]
        next_max = np.max(q_table[next_s[0], next_s[1]])
        q_table[curr[0], curr[1], action] = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        
        curr = next_s

# --- CHẠY THỬ (INFERENCE) ---
print("Đang chạy thử mô hình sau khi train...")
curr = MESSI_START
path_map = np.full((SIZE, SIZE), ' . ')
for r, c in DEFENDERS: path_map[r, c] = ' X ' # Hậu vệ
path_map[GOAL] = ' GO' # Goal
path_map[MESSI_START] = ' M ' # Messi

steps = 0
while curr != GOAL and steps < 20:
    # Chọn hành động tốt nhất dựa trên Q-table
    action = np.argmax(q_table[curr[0], curr[1]])
    
    next_curr, _, done = get_next_state(curr, action)
    path_map[curr] = ' ' + ACTIONS[action][0] + ' ' # Đánh dấu hướng đi
    curr = next_curr
    steps += 1
    if curr in DEFENDERS:
        print("Messi bị hậu vệ chặn mất rồi!")
        break

# Hiển thị sân bóng
for row in path_map:
    print("".join(row))

print(f"\nMessi đã về đích sau {steps} bước!")
print("(M: Messi, X: Hậu vệ, GO: Goal, U/D/L/R: Hướng di chuyển)")
