"""
>>> calc_protein_mass('SKADYEK')
821.38

>>> calc_protein_mass('aaA')
213.12

>>> calc_protein_mass('')
0
"""

AA_MASS = {
    'G': 57.02, 'A': 71.04, 'S': 87.03,
    'P': 97.05, 'V': 99.07, 'T': 101.05,
    'C': 103.01, 'I': 113.08, 'L': 113.08,
    'N': 114.04, 'D': 115.03, 'Q': 128.06,
    'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10,
    'Y': 163.06, 'W': 186.08
}

def calc_protein_mass(P):
    """Calculate the mass of a given protein sequence."""

    P = P.upper()
    total_mass = 0

    for protein in P:
        total_mass += AA_MASS.get(protein)

    return total_mass


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("ALL TESTS PASSED")