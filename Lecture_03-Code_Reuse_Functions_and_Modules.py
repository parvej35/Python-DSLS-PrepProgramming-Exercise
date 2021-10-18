
import rev_comp


if __name__ == "__main__":
    rev_comp.print_input()

    reversed_seq = rev_comp.reverse_dna_seq("CGTTATACAAGTATCTGCTCAATTAGTCGACT")
    print("Reversed DNA sequence : " + reversed_seq)

    complemented_seq = rev_comp.get_complement("CGTTATACAAGTATCTGCTCAATTAGTCGACT")
    print("Complemented sequence : " + complemented_seq)
