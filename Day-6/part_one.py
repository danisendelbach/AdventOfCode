from input import get_input

input, start_pos, init_dir = get_input()

directions = {
    "^": [0, -1],
    ">": [1, 0],
    "v": [0, 1],
    "<": [-1, 0]
}

height = len(input)
width = len(input[0])
visited_fields = [[False for _ in range(width)] for _ in range(height)]

cur_pos = list(start_pos) 
cur_direction = directions[init_dir]
result = 1
visited_fields[cur_pos[1]][cur_pos[0]] = True

while (0 <= x_ahead < width and 0 <= y_ahead < height):
    x, y = cur_pos  
    x_ahead = x + cur_direction[0]
    y_ahead = y + cur_direction[1]

    
    while 0 <= x_ahead < width and 0 <= y_ahead < height and input[y_ahead][x_ahead]:
        cur_pos = [x_ahead, y_ahead]  
        if not visited_fields[y_ahead][x_ahead]:
            result += 1
        visited_fields[y_ahead][x_ahead] = True
        x_ahead = cur_pos[0] + cur_direction[0]
        y_ahead = cur_pos[1] + cur_direction[1]

    cur_direction = [-cur_direction[1], cur_direction[0]]
