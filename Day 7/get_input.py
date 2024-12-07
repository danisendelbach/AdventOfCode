import requests

#get input from advent of code site
def get_input():
    URL = "https://adventofcode.com/2024/day/7/input"
    session = requests.Session()

    cookie = {'session': '<my sessesion cookie>'}
    response = session.get(URL,cookies=cookie)
    lines=response.text.split('\n')
    input={}
    for line in lines:
        if line=='':
            break
        entry=line.split(':')
        equation_res=int(entry[0])
        equation_values=[int(val) for val in entry[1].split(' ')[1:]]
        input[equation_res]=equation_values
    return input