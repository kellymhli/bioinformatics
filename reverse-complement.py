"""
>>> reverse_comp('AAAACCCGGT')
'ACCGGGTTTT'

>>> reverse_comp('')
''
"""
COMP_DICT = {
    'A': 'T', 'T': 'A',
    'G': 'C', 'C': 'G'
    }


def reverse_comp(seq):
    """Return the reverse complement of a DNA sequence."""

    rev = ''

    i = len(seq) - 1
    while i >= 0:
        rev += COMP_DICT.get(seq[i])
        i -= 1

    return rev


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        pass

    seq = input("Enter DNA seq: ").upper()
    while seq != 'Q':
        print(f'         DNA: {seq}')
        print(f'Reverse Comp: {reverse_comp(seq)}')
        seq = input("Enter another DNA seq or q to quit: ").upper()