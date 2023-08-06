def rev_comp(seq):
    comp = str.maketrans("ATGC", "TACG")
    return seq.translate(comp)[::-1]


class NoRecordsException(Exception):
    """No Record found in the sequence file"""

    pass
