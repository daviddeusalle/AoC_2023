
def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def one_star(lines):
    count = 0
    for line in lines: 
        start = end = '0'
        for c in line:
            if c.isdigit():
                if start == '0':
                    start = c
                end = c
       
        count += int(start + end)
    return count 

lines = read('input.txt')
print(one_star(lines))



            
