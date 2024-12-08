from input import get_input

#####very ugly solution


input, start_pos, init_dir = get_input()

directions = {
    "^": [0, -1],
    ">": [1, 0],
    "v": [0, 1],
    "<": [-1, 0]
}


def find_way_out(looking_for_placements):
    height = len(input)
    width = len(input[0])
    visited_fields = [[False for _ in range(width)] for _ in range(height)]

    cur_pos = list(start_pos) 
    cur_direction = directions[init_dir]
    
    visited_fields[cur_pos[1]][cur_pos[0]] = True

    

    possible_coordinates=[]
    turning_points=[]
    counter=0
    good_obstacle=False
    
    while True:
        
        x, y = cur_pos  
        x_ahead = x + cur_direction[0]
        y_ahead = y + cur_direction[1]

        
        while 0 <= x_ahead < width and 0 <= y_ahead < height and input[y_ahead][x_ahead]:
            cur_pos = [x_ahead, y_ahead]  
            counter+=1
            if not visited_fields[y_ahead][x_ahead] and looking_for_placements:
                possible_coordinates.append([x_ahead,y_ahead])
                
            visited_fields[y_ahead][x_ahead] = True
            
            x_ahead = cur_pos[0] + cur_direction[0]
            y_ahead = cur_pos[1] + cur_direction[1]
        
    
        if not (0 <= x_ahead < width and 0 <= y_ahead < height) :
            break
        if [cur_pos,cur_direction] in turning_points:
            good_obstacle=True
            break

        turning_points.append([cur_pos,cur_direction])
        cur_direction = [-cur_direction[1], cur_direction[0]]
    return possible_coordinates,good_obstacle


#bruteforce all possible placements
result=0
placements,_=find_way_out(True)
for placement in placements:
    input[placement[1]][placement[0]]=False
    _, good_obstacle = find_way_out(False)
    if good_obstacle:
        result+=1
    input[placement[1]][placement[0]]=True
print(result)