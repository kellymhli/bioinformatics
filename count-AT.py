def at_content(dna):
    dna_upper = dna.upper()
    num_A = dna_upper.count("A")
    num_T = dna_upper.count("T")
    return ((num_A + num_T)/ len(dna_upper))

if __name__ == "__main__":
    dna = input("Enter a DNA sequence: ")
    while dna != "q" and dna != "Q":
        print(dna)
        at = at_content(dna)
        print (f"AT content = {at:0.3f}")
        dna = input("Enter another DNA sequence (or Q to quit): ")
    