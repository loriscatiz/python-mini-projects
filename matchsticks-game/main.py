def main():
    #hoisting: assegnazione di una variabile e del suo tipo. num_fimmiferi è uno spazio di memoria (variabiile tipo intero, contiene valore 11)
    #python è case sensitive e debolmente tipizzato
    num_matchsticks: int = 11
    current_turn: int = 1
    max_extraction: int = 3
    while num_matchsticks > 1:
        print("Player " + ("2" if current_turn % 2 == 0 else "1") + "'s turn")
        da_estrarre = int(input("Insert number of matchsticks to extract: "))
        while (da_estrarre < 1 or da_estrarre > max_extraction):
            print("Error")
            da_estrarre = int(input("Insert number of matchsticks to extract: "))  
        num_matchsticks = num_matchsticks - da_estrarre
        if(num_matchsticks <= 3): max_extraction = num_matchsticks-1;
        current_turn = current_turn + 1
        print("Remaining matchsticks: ", num_matchsticks)
        if(num_matchsticks <= 1):
            print("Game ends")
            print("Player " + ("1" if current_turn % 2 == 0 else "2") + "wins")


# This is like html index 
if __name__ == "__main__":
    main()

