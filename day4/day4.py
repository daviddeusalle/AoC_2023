

def one_star(filename): 
    with open(filename, 'r') as file: 
        lines = file.readlines()
        res = 0
        for line in lines:
            acc = 0

            sections = line.split(': ')
            sections = sections[1].split(' | ')
            winning = sections[0].split(' ')
            winning = [element for element in winning if element != '']
            sections[1] = sections[1].strip()
            numbers = sections[1].split(' ')
            map = {key: 0 for key in winning}
            for number in numbers: 
                if number in map: 
                    if acc < 2:
                    
                        acc += 1
                        continue
                    acc *= 2
            res += acc
        return res


print('Part 1:', one_star('input.txt'))
