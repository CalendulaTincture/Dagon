def line(number, param):
    line_number = 0
    while number > (line_number * (line_number + 1)) // 2:
        line_number += 1
    start = (line_number * (line_number - 1)) // 2 + 1
    line_length = 0
    for j in range(start, min((line_number * (line_number + 1)) // 2 + 1, n + 1)):
        line_length += len(str(j)) + 1
    line_length -= 1
    position = number - start + 1
    if param == 1:
        return line_length
    elif param == 2:
        return line_number - 1
    elif param == 3:
        return start
    elif param == 4:
        return position


new_line_trigger = 1
line_length_add = 2
n = int(input())
last_start = line(n, 3)
last_line_length = line(n, 1)
current_line_length = 1
current_line_number = 1
for i in range(1, n + 1):
    if i == new_line_trigger:
        new_line_trigger += line_length_add
        line_length_add += 1
        if line(i, 4) == 1:
            current_line_length = line(i, 1)
            current_line_number = line(i, 2)
            current_start = line(i, 3)
            space = (last_line_length - current_line_length) // 2
            print(f'{i: >{space + len(str(i))}}')
        elif line(i, 4) > min(line(i + 1, 4), line(n, 4)):
            current_line_length = line(i, 1)
            current_line_number = line(i, 2)
            current_start = line(i, 3)
            space = (last_line_length - current_line_length) // 2 + (last_line_length - current_line_length) % 2
            print(f'{i: <{space + len(str(i))}}')
        else:
            print(i)
    else:
        if line(i, 4) == 1:
            current_line_length = line(i, 1)
            current_line_number = line(i, 2)
            current_start = line(i, 3)
            space = (last_line_length - current_line_length) // 2
            print(f'{i: >{space + len(str(i))}}', end=' ')
        elif line(i, 4) > line(i + 1, 4):
            current_line_length = line(i, 1)
            current_line_number = line(i, 2)
            current_start = line(i, 3)
            space = (last_line_length - current_line_length) // 2 + (last_line_length - current_line_length) % 2
            print(f'{i: <{space + len(str(i))}}', end=' ')
        else:
            print(i, end=' ')
