"""
Contains all possible nuclotides only
>>> is_valid_seq("ATCGGACTA")
True

Contains random characters
>>> is_valid_seq("ABC;'DEFG")
False

Subset of nucleotides
>>> is_valid_seq("CGGGC")
True

>>> is_valid_seq("")
False
"""

def is_valid_seq(seq):
    """Determine if a sequence contains only valid nucleotides."""

    if seq == "":
        return False

    valid_chars = {"A", "C", "G", "T"}
    seq_set = set(list(seq))

    if seq_set.issubset(valid_chars):
        return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("All tests passed.")

    seq = input("Enter a sequence (or q to quit):\n> ")

    while seq.upper() not in {"Q", "q"}:
        if is_valid_seq(seq.upper()):
            print("Yep, that is a valid DNA sequence.")
        else:
            print("Nope, not a valid DNA sequence.")
        seq = input("\nEnter another sequence (or q to quit):\n> ")