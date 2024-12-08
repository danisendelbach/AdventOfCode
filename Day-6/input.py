import requests

#get input from advent of code site
def get_input():
    URL = "https://adventofcode.com/2024/day/6/input"
    session = requests.Session()

    cookie = {'session': '<my session cookie>'}
    response = session.get(URL,cookies=cookie)
    lines=response.text.split('\n')
    

    height=len(lines)-1
    width=len(lines[0])
    input = [[True for _ in range(width)] for _ in range(height)]
    start_pos=[0,0]
    init_dir=""
    
    
    
    for y in range(height):
        for x in range(width):
            if lines[y][x]=='#':
                input[y][x]=False
            elif lines[y][x]!='.':
                start_pos=[x,y]
                
                init_dir=lines[y][x]
            

    
    return input,start_pos,init_dir