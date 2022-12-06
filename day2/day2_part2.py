def round_simulation(oponent_letter: str, gamer_letter: str) -> int:
    
    points, win = -1, -1

    match gamer_letter:
        case 'Y': 
            win = 3
            if(oponent_letter == 'A'):
                points = 1
            elif(oponent_letter == 'C'):
                points = 3
            else:
                points = 2
        case 'X': 
            win = 0
            if(oponent_letter == 'C'):
                points = 2
            elif(oponent_letter == 'B'):
                points = 1
            else:
                points = 3
        case 'Z': 
            win = 6
            if(oponent_letter == 'B'):
                points = 3
            elif(oponent_letter == 'A'):
                points = 2
            else:
                points = 1

    return points+win



rounds = []

with open("input.txt") as f:
    rounds = f.read().replace(" ", "\n")

rounds = rounds.splitlines()
all_rounds_points = sum([round_simulation(rounds[i],rounds[i+1]) for i in range(0,len(rounds)-1,2)])
print("Total score: ", all_rounds_points)
        
