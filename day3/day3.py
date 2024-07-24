

def read(filename):
    array = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            array.append(list(line))
    return array

def explore(i, j):
    if 0 <= i < len(array) and 0 <= j < len(array[0]):
        if array[i][j].isdigit():
            return explore(i -1, j+1) or explore(i +1, j+1) or explore(i,j + 1)
        if array[i][j] == '.':
            return False
        return True

def one_star():
    res = 0
    add = False
    num = ''
    for i, row in enumerate(array): 
        for j, c in enumerate(row):
            if add:
                if c.isdigit():
                    num += c
                if not c.isdigit() or j == len(row) -1:
                    res += int(num)
                    add = False
                    num = ''

                continue

            if not c.isdigit():
                continue
            if explore(i-1, j) or explore(i-1, j-1) or explore(i+1, j-1) or explore(i +1, j) or explore(i,j-1) or explore(i,j + 1) or explore( i-1, j +1) or explore(i +1 ,j+1):
                add = True
                num += c


    return res


def search(i, j):
    if visited[i][j]:
        return ''

    visited[i][j] = True
    if array[i][j].isdigit():
        return search(i, j -1) + array[i][j] + search(i, j+1)
    return ''

def multiply(values):
    if len(values) != 2: 
        return 0
    res = 1
    for value in values:
        res *= value
    
    return res

def two_star():
    res = 0
    for i, row in enumerate(array): 
        for j, c in enumerate(row):
            if c == '*':
                values = []
                for k in range(i -1, i +2):
                    for l in range(j -1, j+2):
                        aux = search( k, l)
                        if aux.isdigit():
                            values.append(int(aux))
                res += multiply(values)

    return res


array = read('input.txt')


print('Part 1:', one_star())

visited = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
print('Part 2:', two_star())
