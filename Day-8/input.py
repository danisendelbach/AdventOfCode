import requests

#get input from advent of code site
def get_input():
    URL = "https://adventofcode.com/2024/day/8/input"
    session = requests.Session()

    cookie = {'session': '<my session cookie>'}
    response = session.get(URL,cookies=cookie)
    lines=response.text.split('\n')
    #lines="............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............"
    #lines=lines.split('\n')
    input={}
    height=len(lines)-1
    width=len(lines[0])
    for y in range(height):
        for x in range(width):
            val=lines[y][x]
            if val!='.':
                if val not in input:
                    input[val]=[[x,y]]
                else:
                    input[val].append([x,y])
    return input, height, width
    
