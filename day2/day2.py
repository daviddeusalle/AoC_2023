
def one_star(filename):
    res = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            possible = True
            array = [0] * 3
            semi = line.split(': ')
            sets = semi[1].split('; ')
            for s in sets:
                cubes = s.split(', ')
                for cube in cubes:
                    cube = cube.strip()
                    val = cube.split(' ')
                    if val[1] == 'red' and int(val[0]) > 12:
                        possible = False
                    elif val[1] == 'green' and int(val[0]) > 13:
                        possible = False
                    elif val[1] == 'blue' and int (val[0]) > 14:
                        possible = False

            if possible:
                res += i + 1
    return res

def two_star(filename):
    res = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            array = [0] * 3 # RED, GREEN, BLUE
            semi = line.split(': ')
            sets = semi[1].split('; ')
            for s in sets: 
                cubes = s.split(', ')
                for cube in cubes:
                    cube = cube.strip()
                    val = cube.split(' ')
                    if val[1] == 'red':
                        array[0] = max(array[0], int(val[0]))
                    elif val[1] == 'green':
                        array[1] = max(array[1], int(val[0]))
                    elif val[1] == 'blue':
                        array[2] = max(array[2], int(val[0]))
            print(array)
            res += array[0] * array[1] * array[2]
    return res

print("Part 1:", one_star('input.txt'))
print("Part 2:", two_star('input.txt'))
