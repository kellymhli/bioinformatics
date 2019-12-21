"""
This program computes the AT content of a user entered DNA sequence.

>>> at_content("AA")
1.0

>>> at_content("AGGTTC")
0.5

>>> at_content("GACC")
0.25

"""
def at_content(dna):
    num_A = dna.count("A")
    num_T = dna.count("T")
    return ((num_A + num_T)/ len(dna))


if __name__ == "__main__":

    import doctest
    if doctest.testmod().failed == 0:
        pass

    dna = input("Enter a DNA sequence: ").upper()
    while dna != "Q":
        at = at_content(dna)
        print (f"AT content of '{dna}' = {at:0.3f}")
        dna = input("Enter another DNA sequence (or Q to quit): ").upper()
