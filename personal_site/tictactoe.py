# Unit 1 - Introduction: Ponder and Prove - Week 1
# Author - Rebecca Roeth

def main():
    places = {
        1: 1, 
        2: 2, 
        3: 3, 
        4: 4, 
        5: 5, 
        6: 6, 
        7: 7, 
        8: 8, 
        9: 9
    }
    print_board(places)

    while finish(places) == False:
        if finish(places) == False:
            answer = int(input("x's turn to choose a square (1-9): "))

            while check_validity(answer, places) != True:
                answer = int(input("Please enter another space: "))

            places[answer] = "X"
            print_board(places)
        
        if finish(places) == False:
            answer = int(input("o's turn to choose a square (1-9): "))
            while check_validity(answer, places) != True:
                answer = int(input("Please enter another space: "))
            places[answer] = "O"
            print_board(places)
            # to make sure the game hasn't ended yet

    print("Good game. Thanks for playing!")


def check_validity(answer, places):
    # To check if the chosen place isn't already taken
    if places[answer] == "O" or places[answer] == "X":
        return False
    else:
        if answer not in range(1, 10):
            return False
        else:
            return True

def print_board(places):
    print(f"{places[1]}|{places[2]}|{places[3]}")
    print("-+-+-")
    print(f"{places[4]}|{places[5]}|{places[6]}")
    print("-+-+-")
    print(f"{places[7]}|{places[8]}|{places[9]}")

def finish(places):
    # Calculates if the game is over and says who won
    if places[1] == places[2] and places[2] == places[3]:
        return True
    elif places[4] == places[5] and places[5] == places[6]:
        return True
    elif places[7] == places[8] and places[8] == places [9]:
        return True
    elif places[1] == places[4] and places[4] == places[7]:
        return True
    elif places[2] == places[5] and places[5] == places[8]:
        return True
    elif places[3] == places[6] and places[6] == places[9]:
        return True
    elif places[1] == places[5] and places[5] == places[9]:
        return True
    elif places[3] == places[5] and places[5] == places[7]:
        return True

    # If game not over
    else:
        return False

if __name__ == "__main__":
    main()