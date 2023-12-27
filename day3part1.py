def open_file():
    list = []
    with open("input.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            list.append(line)
    return(list)

def makebox(x, y, length):
    #box length is x-1, y-1 to x+length+1 y+1
    xx = x-1
    yy = y-1
    if xx < 0:
        xx = 0
    if yy < 0:
        yy = 0
    endx = x + length
    if endx > 139:
        endx = 139
    endy = y + 1
    if endy > 139:
        endy = 139
    for y1 in range(yy, endy + 1):
        for x1 in range(xx,endx + 1):
            symbol = findsymbol(x1,y1)
            if symbol.isdigit() == False and symbol != ".":
                return(True)
    return(False)
def findsymbol(x, y):
    symbol = list[y][x]
    return(symbol)

def getlength(x,y):
    xx = x + 1
    if xx > 139:
        return(1)
    length = 1
    while findsymbol(xx,y).isdigit():
        length += 1
        xx += 1
        if xx > 139:
            break
    return(length)  

        
    
def findnum(list):
    sum = 0
    for y in range(len(list)):
        x = 0
        while x <= 139:
            
            if findsymbol(x,y).isdigit():
                length = getlength(x,y)
                if makebox(x,y,length):
                    numbr = ""
                    for i in range(length):
                        numbr += findsymbol(x+i,y)
                    number = int(numbr)
                    sum += number
                    #print(f'x: {x}, y: {y} length: {length} sum: {sum} number: {number}')
                x += length -1
            x += 1
    return(sum)
                    
if __name__ == "__main__":
    list = open_file()
    print(findnum(list))
