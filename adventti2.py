def get_list():
    file = open("input2.txt", "r")
    document = file.read()
    file.close()
    lst = document.split(sep = "\n")
    return(lst)


#function that turns a game into a list of lists with ["number", "color"]

def gametolist(game :str):
    list = game[(game.find(":"))+2:]
    list = list.replace(";", "")
    list = list.replace("," , "")
    list = list.split(" ")
    

    for i in range(len(list)):
        if i % 2 == 0:
            if list[i+1] == "red":
                if int(list[i]) > 12:
                    return(False)
            if list[i+1] == "green":
                if int(list[i]) > 13:
                    return(False)
            if list[i+1] == "blue":
                if int(list[i]) > 14:
                    return(False)
    return(True)

def findmaxcolors(game: str):
    list = game[(game.find(":"))+2:]
    list = list.replace(";", "")
    list = list.replace("," , "")
    list = list.split(" ")
    highest = [0, 0, 0] ## red, green, blue
    for i in range(len(list)):
        if i % 2 == 0:
            if list[i + 1] == "red":
                if int(list[i]) > int(highest[0]):
                    highest[0] = int(list[i])
            if list[i+1] == "green":
                if int(list[i]) > int(highest[1]):
                    highest[1] = int(list[i])
            if list[i+1] == "blue":
                if int(list[i]) > int(highest[2]):
                    highest[2] = int(list[i])
    return(highest)



def game1():
    sum = 0
    for i in range(100):
        if gametolist(the_list[i]) == True:
            sum += i+1
    print(sum)
            
    
#function to use findmaxcolors result [red, green, blue]
def game2(game :str):
    tulos = (int(game[0]) * int(game[1]) * int(game[2]))
    return(tulos)

#function to do all the lines and add the results
def endgame(list):
    result = 0
    for i in range(len(list)-1):
        result += game2(findmaxcolors(list[i]))
    print(result)
        
    
if __name__ == "__main__":
    testi = "Game 1: 3 blue, 13 red; 1 red, 2 green, 6 blue; 2 green"
    bag = [["12", "red"], ["13", "green"], ["14", "blue"]]
    the_list = get_list()
    #print(findmaxcolors(testi))
    #print(game2(findmaxcolors(testi)))
    game1()
    endgame(the_list)
