from os import truncate
from typing import OrderedDict


def main():

    filename = "PuzzleDay5Input.txt"
    lines = parse_file_and_get_lines(filename)
    
    diagram = build_diagram_and_mark_with_lines(lines)

    answer=get_points_with_atleast_two_lines(diagram)
    
    
    print("GURJYOT", answer)

def get_points_with_atleast_two_lines(diagram):
    count = 0
    for row in diagram:
        for num in row:
            if num>1:
                count+=1
    return count

def parse_file_and_get_lines(filename):
    lines=[]
    file = open(filename, "r")
    for line in file:
        fro, to = line.split('->')[0], line.split('->')[1]
        fro, to = fro.strip().split(','), to.strip().split(',')
        x1,y1,x2,y2=int(fro[0]), int(fro[1]), int(to[0]), int(to[1])
        lines.append((x1,y1,x2,y2))

    file.close()
    return lines

def build_diagram_and_mark_with_lines(lines):
    diagram = [ [0] * 1000 for _ in range(10000)]
    for line in lines:
        
        # X1=X2, Vertical line
        if line[0]==line[2]:
            diagram = mark_diagram_with_vertical_line(diagram, line[1], line[3], line[0])
        
        # Y1=Y2, horizontal line
        elif line[1]==line[3]:
            diagram = mark_diagram_with_horizontal_line(diagram, line[0], line[2], line[1])
        else:
            diagram = mark_diagram_with_diagonal_line(diagram, line[0], line[1], line[2], line[3])
    return diagram


def mark_diagram_with_diagonal_line(diagram, x1, y1, x2, y2):
    y_inc = True if y2 > y1 else False
    x_inc = True if x2>x1 else False
    y_to=y2
    x_to=x2
    y = y1
    x = x1

    while y!=y_to and x!=x_to:
        diagram[y][x] += 1
        x = x+1 if x_inc else x-1
        y= y+1 if y_inc else y-1
    
    diagram[y][x] += 1
    return diagram

def mark_diagram_with_horizontal_line(diagram, y1, y2, x):
    y_from=min(y1, y2)
    y_to=max(y1, y2)
    y = y_from
    while y<=y_to:
        diagram[x][y] += 1
        y+=1
    return diagram


def mark_diagram_with_vertical_line(diagram, x1, x2, y):
    x_from=min(x1, x2)
    x_to=max(x1, x2)
    x = x_from
    while x<=x_to:
        diagram[x][y] += 1
        x+=1
    return diagram

if __name__ == "__main__":
    main()
