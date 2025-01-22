def main():
    g1 = input("Player 1: R = Rock, P = Paper, S = Scissors: ")
    g2 = input("Player 2: R = Rock, P = Paper, S = Scissors: ") 

    winner = "Giocatore 2"
    if g1 == g2: 
        winner = "Draw"
    elif g1 == "P" and g2 == "R":
        winner = "Giocatore 1"
    elif g1 ==  "R" and g2 == "S":
        winner = "Giocatore 1"
    elif g1 == "S" and g2 == "P":
        winner = "Giocatore 1"

    print (winner)

if __name__ == "__main__":
    main()