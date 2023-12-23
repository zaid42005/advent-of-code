import re
class scenarioSet:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __str__(self) -> str: #printing out the object
        return str ((self.red,self.green,self.blue))
    def __repr__ (self):
        return str ((self.red,self.green,self.blue)) # redefining repr and str both to print the object
    def isPossible(self, other): #compare
        return (self.red <= other.red and self.green <= other.green and self.blue <= other.blue)

def parsing(scenario):
    colors = ["red","green","blue"]
    values = [0,0,0]
    # eg 4 red , 3 green , 5 blue
    for token in scenario.split(","):
        #["4 red","3 green","5 blue"]
        for i, color in enumerate(colors):
            if color in token:
                values[i] += int(token.split()[0]) # split 4 red into ["4","red"] then take the corresponding color value and put it in the values array [0] since the first vaule in split is always the number
        # neat trick return scenarioSet(*values)
    return scenarioSet(values[0],values[1],values[2])


def main(input):
    total = scenarioSet(12,13,14)
    part1 = 0
    for game_num, line in enumerate(input.splitlines()):
        game_num +=1 
        _, rhs = line.split(":") #this splits the Game 1 away from the rest of it (who came up with this shit goddamn)
        sets = []
        for scenario in rhs.split(";"): #this splits the scenarios up 
            sets.append(parsing(scenario))
        if all (s.isPossible(total) for s in sets):
            part1 += game_num
    return part1


print(main(open("games.txt","r").read()))
