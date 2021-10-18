def print_input():
    given_string = input("Write something : ")
    print("You Wrote: " + given_string)


def reverse_dna_seq(dna_sequence):
    return dna_sequence[::-1]


def get_complement(dna_sequence):
    dna_seq_list = []
    MOLECULES_REPLACING_DICT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    for i in dna_sequence:
        dna_seq_list.append(MOLECULES_REPLACING_DICT[i])

    return ''.join(dna_seq_list)