#DNA base complementary
bases = input("Insert a sample DNA strand: ")
for base in bases:
    if base == "C": print("G", end="")
    elif base == "T": print("A", end="")
    elif base == "A": print("T", end="")
    elif base == "G": print("C", end="")
    else: 
        bases = False
        print("Invalid Input") 
        break