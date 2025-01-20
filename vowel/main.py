def get_valid_char():

    while True:

        try:
            retvalue = input("Insert a letter: ")
            if len(retvalue) > 1:
                raise ValueError("Longer than 1 char")
            if len(retvalue) == 0:
                raise ValueError("Empty string")
            if not retvalue.isalpha():
                raise ValueError("Not a letter")
            return retvalue.lower()
        
        except ValueError as e:
            if str(e) == "Longer than 1 char":
                print("That's more than one charachter")
            if str(e) == "Not a letter":
                print("That's not a letter")
            if str(e) == "Empty string":
                print("You didn't type anything")

def main():
    vowels = list("aeiou")
    char = get_valid_char()
    
    if char in vowels:
        print(char, "is a vowel")
    else:
        print(char, "is not a vowel")

if __name__ == "__main__":
    main()