from input import get_input

input, height, width=get_input()
antinodes_map = [[False for _ in range(width)] for _ in range(height)]

def generate_antinodes(antenna1, antenna2):
    x_dist=antenna1[0]-antenna2[0]
    y_dist=antenna1[1]-antenna2[1]

    antinode1=[antenna1[0]-2*x_dist, antenna1[1]-2*y_dist]
    antinode2=[antenna2[0]+2*x_dist, antenna2[1]+2*y_dist]

    return antinode1, antinode2

def out_of_bound(coor):
    return coor[0]<0 or coor[0]>=width or coor[1]<0 or coor[1]>=height

def antinodes_within_frequency(antennas, index):
    if index>=len(antennas)-1:
        return []
    antinodes=[]
    for i in range(index+1,len(antennas)):
        antinode1, antinode2=generate_antinodes(antennas[index],antennas[i])
    
        if not out_of_bound(antinode1) and not antinodes_map[antinode1[1]][antinode1[0]]:
            antinodes.append(antinode1)
            antinodes_map[antinode1[1]][antinode1[0]]=True

        if not out_of_bound(antinode2) and not antinodes_map[antinode2[1]][antinode2[0]]:
            antinodes.append(antinode2)
            antinodes_map[antinode2[1]][antinode2[0]]=True
            
    return antinodes + antinodes_within_frequency(antennas,index+1)



all_antinodes=[]
for frequency, antennas in input.items():
    
    antinodes_of_frequency=antinodes_within_frequency(antennas,0)
    all_antinodes+=(antinodes_of_frequency)
    

print(len(all_antinodes))


