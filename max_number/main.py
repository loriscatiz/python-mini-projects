def main():

    def get_valid_input(prompt: str):
        while True:
            try: return float(input(prompt))
            except ValueError: print("Please, insert a valid value")

    x1 = get_valid_input("Insert first number: ")
    x2 = get_valid_input("Insert second number: ")

    if x1 > x2: 
        print(x1, "is greater than", x2)
    elif x1 < x2: 
        print(x2, "is greater than", x1)
    else: 
        print(x1, "and", x2, "are equal")

if __name__ == "__main__":
    main()