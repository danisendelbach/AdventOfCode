from input import get_input

input, height, width=get_input()
antinodes_map = [[False for _ in range(width)] for _ in range(height)]


def generate_antinodes(cur, next):
    antinodes_of_two_antennas=[]
    x_dist=cur[0]-next[0]
    y_dist=cur[1]-next[1]
    cache=[next[0],next[1]]
    next=[cur[0]-2*x_dist, cur[1]-2*y_dist]
    cur=[cache[0],cache[1]]
    
    while not out_of_bound(next) :   
        if not antinodes_map[next[1]][next[0]]:
            antinodes_map[next[1]][next[0]]=True
            antinodes_of_two_antennas.append([next[0],next[1]])
        x_dist=cur[0]-next[0]
        y_dist=cur[1]-next[1]
        cache=[next[0],next[1]]
        next=[cur[0]-2*x_dist, cur[1]-2*y_dist]
        cur=[cache[0],cache[1]]
    
    return antinodes_of_two_antennas


def out_of_bound(coor):
    return coor[0]<0 or coor[0]>=width or coor[1]<0 or coor[1]>=height


def antinodes_within_frequency(antennas, index):
    if index>=len(antennas):
        return []
    antinodes=[]
    if not antinodes_map[antennas[index][1]][antennas[index][0]]:
        antinodes_map[antennas[index][1]][antennas[index][0]]=True
        antinodes.append([antennas[index][1],antennas[index][0]])
    for i in range(index+1,len(antennas)):
        
        antinodes+=generate_antinodes(antennas[index],antennas[i])
        antinodes+=generate_antinodes(antennas[i],antennas[index])
        

    return antinodes + antinodes_within_frequency(antennas,index+1)



all_antinodes=[]
for frequency, antennas in input.items():
    
    antinodes_of_frequency=antinodes_within_frequency(antennas,0)
    all_antinodes+=(antinodes_of_frequency)
    
print(len(all_antinodes))