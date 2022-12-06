def round_simulation(oponent_letter: str, gamer_letter: str) -> int:
    # Y Paper - 2;
    # Z Scissors - 3
    # X Rock - 1

    # Oponent:
    # B Paper
    # C Scissors
    # A Rock

    points, win = -1, -1

    match gamer_letter:
        case 'Y': 
            points = 2
            if(oponent_letter == 'A'):
                win = 6
            elif(oponent_letter == 'C'):
                win = 0
            else:
                win = 3
        case 'X': 
            points = 1
            if(oponent_letter == 'C'):
                win = 6
            elif(oponent_letter == 'B'):
                win = 0
            else:
                win = 3
        case 'Z': 
            points = 3
            if(oponent_letter == 'B'):
                win = 6
            elif(oponent_letter == 'A'):
                win = 0
            else:
                win = 3

    return points+win



rounds = []

with open("input.txt") as f:
    rounds = f.read().replace(" ", "\n")

rounds = rounds.splitlines()
all_rounds_points = sum([round_simulation(rounds[i],rounds[i+1]) for i in range(0,len(rounds)-1,2)])
print("Total score: ", all_rounds_points)
        
